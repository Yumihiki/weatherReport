# coding: utf-8
""" LINEのプッシュ通知を送る"""
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

import main
import env

LINE_BOT_API = LineBotApi(env.CHANNEL_ACCESS_TOKEN)


def push():
    """ プッシュ通知をする"""
    try:
        LINE_BOT_API.push_message(
            env.SEND_USER_ID,
            TextSendMessage(text=main.main())
        )
    except LineBotApiError as error:
        LINE_BOT_API.push_message(
            env.SEND_USER_ID,
            TextSendMessage(text='エラーが発生しました。作成者に問い合わせてください。')
        )
        print(error)


if __name__ == '__main__':
    push()
