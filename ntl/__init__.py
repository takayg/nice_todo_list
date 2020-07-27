from flask import Flask # 本体のインストール
from flask_sqlalchemy import SQLAlchemy # データベースのインストール

app = Flask(__name__) # アプリケーション本体の作成
app.config.from_object('ntl.config') # configファイルの有効化

db = SQLAlchemy(app) # データベース作成

from ntl.views import users, creators # ビューのインストール

