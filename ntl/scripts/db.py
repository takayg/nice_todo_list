from flask_script import Command
from ntl import db


class InitDB(Command): # スクリプト実行のためのクラス
    "create database" # コメント

    def run(self):
        db.create_all()