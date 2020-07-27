from flask_script import Manager
from ntl import app

from ntl.scripts.db import InitDB


if __name__ == "__main__":
    manager = Manager(app)
    manager.add_command('init_db', InitDB()) # 作成したInitDB()モジュールをinit_dbという名前で実行できる
    manager.run()