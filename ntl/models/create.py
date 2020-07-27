from ntl import db
from datetime import datetime

class Create(db.Model):
    __tablename__ = 'backgrounds'
    id = db.Column(db.Integer, primary_key=True) # 数字からなるidという属性を、primary_keyとして定義,db.Integerは、数字が入るという定義
    title = db.Column(db.String(50), unique=True) # 50文字以内の文字列,一意
    name = db.Column(db.String(50))
    created_at = db.Column(db.DateTime) # 日付
    directory = db.Column(db.String(100))

    def __init__(self, title=None, name=None):
        self.title = title
        self.name = name
        self.created_at = datetime.utcnow()
        self.directory = '/static/images/' + title + '.png'

    def __repr__(self):
        return '<Entry id:{} title:{} name:{} directory:{}>'.format(self.id, self.title, self.name, self.directory)