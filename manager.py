# 啟動文件.py

# 工廠模式
from app import create_app
import os

app = create_app('production') # development/production
port = int(os.environ.get('PORT', 5000))
# app.run(host='0.0.0.0', port=os.environ.get("PORT", 33507)) # HEROKU部署不能用localhost，PORT也要抓他自己生成的
app.run(host='0.0.0.0', port=port)

# print(app.url_map) # 透過app.url_map可以查詢專案所有路由清單，可以用來看執行狀況