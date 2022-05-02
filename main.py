# coding: utf-8
""" 天気情報を取得する"""
import json
import requests

# APIの実行URL
BASE_URL = 'https://weather.tsukumijima.net/api/forecast/city/'
# 以下の情報はhttps://weather.tsukumijima.net/primary_area.xml から取得
# 奈良県 奈良の固定値（天気情報の町）
CITY_ID = '290010'
URL = BASE_URL + CITY_ID
CITY_NAME = '奈良'

# APIでは0番目に当日データが割り振られるため0を当日とする
TODAY = 0

# API送信時のオリジナルヘッダ APIの提供者の方が何のアプリから叩かれているかわかるために定義
HEADERS = {
    'User-Agent': 'weatherReport/1.0'
}


def main(is_local_debug=True):
    """ メインロジック

    :param is_local_debug: 開発環境でデバッグ目的の場合: True
    :return: 天気の情報
    """
    print('---start---')
    try:
        # 提供APIへの負荷軽減のためAPI実行時と同等の結果を持つファイルを利用する
        if is_local_debug:
            with open('sample.json', 'r') as sample_json:
                weather_data = json.load(sample_json)
                print('debug mode')
        else:
            weather_data = requests.get(URL, headers=HEADERS).json()
    except Exception as error:
        print(f'Error! except is {error}')

    try:
        print(f"{CITY_NAME}の天気をお知らせします "
              f"今日は {weather_data['forecasts'][TODAY]['telop']} です")
        print('---finish---')
        return f"{CITY_NAME}の天気をお知らせします " \
               f"今日は {weather_data['forecasts'][TODAY]['telop']} です"
    except Exception as error:
        print(f'Error! except is {error}')


if __name__ == '__main__':
    main(is_local_debug=True)
