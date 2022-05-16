# これは何？
Pythonで天気情報のAPIを叩いて結果を取得するプログラムです。

LINEBotも実装しLINE上で確認することもできます（2022/5/2時点では個人）。

GitHubActionsを利用してherokuへ自動デプロイするようにしています。

# 設定情報について
個人で利用するのを目的としていたため、そのままでは利用できません。
以下の設定を各自で編集・設定することで利用可能になります。
1. env.py の作成及び設定の登録
   1. CHANNEL_ACCESS_TOKEN: LINEのチャンネルアクセストークン 
   2. SEND_USER_ID: 送信先LINEユーザーID
2. GitHub(Actions)
   1. HEROKU_API_KEY: herokuのAPI実行キー
   2. HEROKU_EMAIL: herokuのログインメールアドレス
3. heroku Config Vars
   1. YOUR_CHANNEL_ACCESS_TOKEN
   2. YOUR_CHANNEL_SECRET
4. CITY_ID, CITY_NAMEの修正
   1. main.pyに記載の定数値の修正（コメントに定義元を記載）

# 使用ライブラリ
requirements.txt に記載しています。

# 使用API
## 天気取得
https://weather.tsukumijima.net/

## LINEBot
https://github.com/line/line-bot-sdk-python

# 実行環境
## ローカル
Python3.8
macOS BigSur 11.6.4
## デプロイ先
heroku20

# 実行方法
## ローカルでコンソール出力
python3 main.py
## LINEへプッシュメッセージ送信
python3 push.py

# 出力イメージ
## ローカル
---start---

debug mode

奈良県の天気をお知らせします 今日は 晴のち曇 です

---finish---

## LINE
![LINE](LINEイメージ.PNG)