
from app import db, login # import初始化過的套件
from flask_login import UserMixin # 多重繼承
from flask import current_app, render_template # current_app類似定義user，但是直接連接目前的使用者

# 登錄名單資料表
class UserRegister(UserMixin, db.Model):
    __tablename__ = 'UserRegister' # 資料表名稱
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    vote = db.Column((db.Boolean))

# 登入功能
@login.user_loader
def load_user(user_id):
    return UserRegister.query.get(int(user_id))

# 投票統計
class UserVote(db.Model):
    __tablename__ = 'UserVote' # 資料表名稱
    vid = db.Column(db.Integer, primary_key=True)
    YorN =  db.Column(db.String(5), nullable=False)

    def __init__(self, YorN):
        self.YorN = YorN

    def __repr__(self):
        return 'YorN:%s' % (self.YorN)