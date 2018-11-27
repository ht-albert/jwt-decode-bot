# jwt-decode-bot
Decoder JWT bot


Instructions for use:
1. Add telegram bot [@jwt_bot](https://t.me/jwt_bot)
2. Create JWT-token, and add in `payload` field `tg_username: YOU_TELEGRAM_LOGIN`
3. Send `GET` request on url `https://jwt-bot.herokuapp.com/?jwt={YOU_JWT_TOKEN}` 

The bot will send the decrypted token to your telegram
