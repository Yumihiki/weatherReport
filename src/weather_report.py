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
    'User-Agent': 'weather_report/2.1'
}


def weather_report(is_local_debug=True):
    """ 町の天気のメッセージを返す

    :param is_local_debug: 開発環境でデバッグ目的の場合: True
    :return: 町の天気のメッセージ
    """
    try:
        weather_data = get_weather_data(is_local_debug)
        return f"{weather_data['forecasts'][TODAY]['date']}の" \
               f'{CITY_NAME}の天気をお知らせします'
    except KeyError:
        return '町の天気のメッセージ取得に失敗しました。'


def weather_report_telop(is_local_debug=True):
    """ 天気情報を返す

    :param is_local_debug: 開発環境でデバッグ目的の場合: True
    :return: 天気の情報
    """
    try:
        weather_data = get_weather_data(is_local_debug)
        return f"今日は {weather_data['forecasts'][TODAY]['telop']} です"
    except KeyError:
        return '天気情報の取得に失敗しました（テロップ）。'


def weather_link(is_local_debug=True):
    """ 天気のURLを返す

    :param is_local_debug: 開発環境でデバッグ目的の場合: True
    :return: 天気のURL
    """
    try:
        weather_data = get_weather_data(is_local_debug)
        return weather_data['link']
    except KeyError:
        return '天気情報の取得に失敗しました。（URL）'


def get_weather_data(is_local_debug=True):
    """ 天気情報を取得する

    APIまたはファイルから天気情報を取得する
    APIへの負荷軽減のため、開発時には同等の結果を出力するサンプルファイルを用いる

    :param is_local_debug: 開発環境でデバッグ目的の場合: True
    :return: 天気の情報
    """
    try:
        if is_local_debug:
            with open('src/sample.json', 'r', encoding='utf-8') as sample_json:
                return json.load(sample_json)
        return requests.get(URL, headers=HEADERS).json()
    except FileNotFoundError:
        print('FileNotFoundError, jsonファイルがあるか確認してください。')


if __name__ == '__main__':
    print(weather_report(is_local_debug=True))
    print(weather_report_telop(is_local_debug=True))
    print(weather_link(is_local_debug=True))
