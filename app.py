import datetime
import time

import jwt
import telebot
from flask import Flask, request, abort, redirect

from config import Config

config = Config()
users = {}

if config.is_local:
    telebot.apihelper.proxy = {
        'https': config.proxy
    }

app = Flask(__name__)
bot = telebot.TeleBot(config.bot_token)


@app.route('/')
def hello():
    return redirect(config.bot_doc)


@app.route('/' + config.bot_token, methods=['POST'])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return ''


@app.route('/<int:tg_user>/', methods=['GET'])
def decode_jwt(tg_user):
    token = request.args.get('jwt')
    if not token:
        return abort(400, "Missing param jwt.")
    try:
        decode_info = jwt.decode(token, verify=False)
    except Exception:
        return abort(400, "Invalid jwt token.")
    try:
        bot.send_message(tg_user, 'TOKEN: \n{}'.format(token))
        bot.send_message(tg_user, 'DECODE: \n{}'.format(decode_info))
        bot.send_message(tg_user, '==== {} ===='.format(datetime.datetime.now().replace(microsecond=0)))
    except Exception:
        return abort(400, "Start telegram bot, and use you link.")
    return 'ok'


@bot.message_handler(commands=['start'])
def calendar(mess):
    token = jwt.encode(payload={'message': 'Hello world'}, key='')
    message = """Hello, i send your data:\nYOU LINK: {host}{user}/\nExample:\n{host}{user}?jwt={jwt}
    """.format(host=config.host, user=mess.chat.id, jwt=token)
    bot.send_message(mess.chat.id, 'Documentation:\n{}'.format(config.bot_doc))
    bot.send_message(mess.chat.id, message)


if __name__ == '__main__':
    if config.is_local:
        bot.polling()
    else:
        bot.set_webhook(url=config.host + config.bot_token)
        time.sleep(0.1)
        app.run(host='0.0.0.0', port=config.port, debug=True)
