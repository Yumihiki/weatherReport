# coding: utf-8
""" 天気情報を取得する"""
import requests

import json

# todo: 定数値の別モジュール化
# APIの実行URL, 奈良県 奈良の固定値
# todo: URLの末尾を可変な仕組みにする
URL = 'https://weather.tsukumijima.net/api/forecast/city/290010'

# APIでは0番目に当日データが割り振られるため0を当日とする
TODAY = 0

# API送信時のオリジナルヘッダ
HEADERS = {
    'User-Agent': 'weatherReport/0.0.1'
}


def main(is_local_debug=True):
    """ メインロジック

    :param is_local_debug: 開発環境でデバッグ目的の場合: True
    :return: 天気の情報
    """
    # 提供APIを必要以上に呼ばないため、API実行時と同等の結果を持つファイルを利用する
    print('---start---')

    try:
        if is_local_debug:
            with open('sample.json', 'r') as sample_json:
                weather_data = json.load(sample_json)
                print('debug mode')
        else:
            weather_data = requests.get(URL, headers=HEADERS).json()
    except Exception as e:
        print(f'Error! except is {e}')

    try:
        # todo: URLによって場所を変化させるように（奈良県固定値を直す）
        print(f"奈良県の天気をお知らせします")
        print(f"今日は {weather_data['forecasts'][TODAY]['telop']} です")
        return f"今日は {weather_data['forecasts'][TODAY]['telop']} です"
    except Exception as e:
        print(f'Error! except is {e}')
    print('---finish---')


if __name__ == '__main__':
    main(is_local_debug=True)
