# coding: utf-8
""" LINEのプッシュ通知を送る"""
from linebot import LineBotApi
from linebot.exceptions import LineBotApiError
from linebot.models import TextSendMessage

from env import CHANNEL_ACCESS_TOKEN, SEND_USER_ID
from weather_report import weather_report, weather_report_telop, weather_link

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)


def push():
    """ プッシュ通知をする"""
    try:
        line_bot_api.push_message(
            SEND_USER_ID,
            [TextSendMessage(text=weather_report(is_local_debug=False)),
             TextSendMessage(text=weather_report_telop(is_local_debug=False)),
             TextSendMessage(text=weather_link(is_local_debug=False))]
        )
    except LineBotApiError as error:
        line_bot_api.push_message(
            SEND_USER_ID,
            TextSendMessage(text='エラーが発生しました。作成者に問い合わせてください。')
        )
        print(error)


if __name__ == '__main__':
    push()
