# JWT Decoder Bot
Bot for decoding jwt token. Used for development.


# How to use the bot?
1. Start bot telegram [@jwt_bot](https://t.me/jwt_bot)
2. Bot will send you a link for decode (example `https://your_link.com/you_id/`)
3. Send `GET` request on url `https://your_link.com/you_id/?jwt={YOU_JWT_TOKEN}` (`jwt` required parameter!)


The bot will send the decrypted token to your telegram
