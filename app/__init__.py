# 將LaitGoodProject內所有初始化設置於此(__init__.py)

from flask import Flask
from config import config # 參數設置
from flask_sqlalchemy import SQLAlchemy # 資料庫
from flask_login import LoginManager # flask_login的初始化
# from flask_admin import Admin # 後台管理系統
from flask_wtf.csrf import CSRFProtect # CSRF token，解決來源信任的問題



db = SQLAlchemy()
# admin = Admin(name='後台管理系統')
login = LoginManager()
csrf = CSRFProtect()

def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name]) # 渲染參數

    db.init_app(app) # 資料庫
    # admin.init_app(app) # 後台
    csrf.init_app(app) # csrf

    # 登入相關：
    login.init_app(app)
    login.login_view = 'member.login' # 路由有裝飾login_required時導向此
    login.login_message = "請先登入再進行此操作"


    # Blueprint_member
    from app.member import member
    app.register_blueprint(member, url_prefix='/member') # 網址前綴/member

    # # Blueprint_admins
    # from app.admins import admins
    # app.register_blueprint(admins, url_prefix='/admins') # 網址前綴/admins

    return app
