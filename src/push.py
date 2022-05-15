# coding: utf-8
""" LINEのプッシュ通知を送る"""
from linebot import LineBotApi
from linebot.exceptions import LineBotApiError
from linebot.models import TextSendMessage

from env import CHANNEL_ACCESS_TOKEN, SEND_USER_ID
from main import weather_report

LINE_BOT_API = LineBotApi(CHANNEL_ACCESS_TOKEN)


def push():
    """ プッシュ通知をする"""
    try:
        LINE_BOT_API.push_message(
            SEND_USER_ID,
            TextSendMessage(text=weather_report(is_local_debug=False))
        )
    except LineBotApiError as error:
        LINE_BOT_API.push_message(
            SEND_USER_ID,
            TextSendMessage(text='エラーが発生しました。作成者に問い合わせてください。')
        )
        print(error)


if __name__ == '__main__':
    push()
