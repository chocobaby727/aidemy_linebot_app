# main.py
import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('477ea325208e22becf379592daec33fa')  # アクセストークンを入れてください
handler = WebhookHandler('30wDmlLacfiOmKH9gooYw/S50HwHJ4pw6o0Jy3g+xtNFkcN3Fq62TQkJ4mxzOGPikT17AEurotC4v14MRmUlAxC6zOOdycEmyoCIWNwjOfmrYVL/BPNzlMeHi20Lbg5AhRfAKP/7zc9BbsChl/45bQdB04t89/1O/w1cDnyilFU=')  # Channel Secretを入れてください


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['x-line-signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# テキストメッセージが送信されたときの処理
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='メッセージを受信しました。'))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host ='0.0.0.0',port = port)
