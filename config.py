# 隨機生成資安防護用的金鑰：
# import os
# print (os.urandom(24))

import os
from datetime import timedelta

# SQLite資料庫連線
pjdir = os.path.abspath(os.path.dirname(__file__))
def create_sqlite_uri(db_name):
    return "sqlite:///" + os.path.join(pjdir, db_name)
DATABASE_URI = "postgresql://evqspvzoibbyph:0ea42790b514f2dee5d1414ed82ef6551fa5057f50002f04bc764ce15cd7a423@ec2-54-86-214-124.compute-1.amazonaws.com:5432/dd7qq3kai8fuk7"

class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False # True會追蹤各種改變的信號而消耗額外的記憶體
    SECRET_KEY = '\t>\xf2;\x89\x9d4e\xd1\x89\x8c\x9e\xf9>\xd02"2i.\x83\xf7\x97\x84' # 金鑰

class DevelopmentConfig(BaseConfig): # 開發環境
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = create_sqlite_uri('app\\static\\database\\voteforher_login.sqlite')
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    # 終端機設置 $env:DATABASE_URI = "postgres://HEROKU的API" # HEROKU部署-pg

class TestingConfig(BaseConfig): # 測試環境
    TESTING = True
    WTF_CSRF_ENABLED = False # flask-wtf 用 csrf_token處理 CSRF 的攻擊，測試時不會像正常使用一樣實際按下送出，而是直接傳資料到後端會被 csrf_token 擋下來，所以要關掉。
    # SQLALCHEMY_DATABASE_URI = create_sqlite_uri('app\\static\\database\\voteforher_login.sqlite')
    SQLALCHEMY_DATABASE_URI = DATABASE_URI


class ProductionConfig(BaseConfig): # 正式環境
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    # SQLALCHEMY_DATABASE_URI = create_sqlite_uri('app\\static\\database\\voteforher_login.sqlite')

# 環境配置更換時
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}