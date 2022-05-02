from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

import main
import env

line_bot_api = LineBotApi(env.CHANNEL_ACCESS_TOKEN)


def push():
    try:
        line_bot_api.push_message(
            env.SEND_USER_ID,
            TextSendMessage(text=main.main(False))
        )
    except LineBotApiError as e:
        pass


if __name__ == '__main__':
    push()
