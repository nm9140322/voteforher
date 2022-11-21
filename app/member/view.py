
import datetime
from . import member # blueprint，所有網址都會加上前綴/member (member.)
from app import db # 從__init__.py 引入初始化的app
from flask import render_template, url_for, redirect, flash
from app.member.model import UserRegister, UserVote # 從model.py引入資料表
from app.member.form import  FormRegister, FormLogin, FormVote # 從form.py引入表格
from flask_login import current_user, login_user, logout_user, login_required # 登入功能


# 資料庫操作
@member.route('/', methods=['GET', 'POST'])
def dbtable():
    db.create_all() # 建置table
    return '建置資料庫註冊表'


# 登錄投票名單
@member.route('/register', methods=['GET', 'POST'])
def register():
    totaluser = UserRegister.query.count()
    voteuser = UserRegister.query.filter_by(vote=True).count()

    form = FormRegister(vote = False)
    if form.validate_on_submit():
        user = UserRegister.query.filter_by(email=form.email.data).first()
        if user ==False:
            user = UserRegister( # 實作使用者類別並且賦值
                username = form.username.data,
                email = form.email.data,
                vote = form.vote.data
                )
            db.session.add(user)
            db.session.commit()

            flash('登錄成功')
            return redirect('/member/register')
        else:
            flash('信箱重複')
    else:
        flash('信箱輸入有誤')
    return render_template('register.html', form=form, totaluser=totaluser, voteuser=voteuser)

# 登入投票
@member.route('/login', methods=['GET', 'POST'])
def login():
    totaluser = UserRegister.query.count()
    voteuser = UserRegister.query.filter_by(vote=True).count()
    form = FormLogin()
    if form.validate_on_submit():
        user = UserRegister.query.filter_by(email=form.email.data).first() # 檢核帳號是否存在
        if user: # 使用者存在資料庫
            if user.vote == False:
                login_user(user) # flask-login內建的登入函式
                return redirect('/member/vote')
            else:
                flash('您已經投下神聖的一票囉！若您未進行操作...我們中出了內鬼！！！')
        else:
            flash('信箱不存在，請重新確認。')
    else:
        flash('信箱輸入有誤')
    return render_template('login.html', form=form, totaluser=totaluser, voteuser=voteuser)

# 投完票直接登出
@member.route('/vote', methods=['GET', 'POST'])
@login_required
def vote():
    totaluser = UserRegister.query.count()
    voteuser = UserRegister.query.filter_by(vote=True).count()
    form = FormVote(YorN = 'Y')
    user = UserRegister.query.filter_by(id=current_user.id).first()
    if form.validate_on_submit():
        user.vote = True
        db.session.add(user)
        db.session.commit()

        voted = UserVote(form.YorN.data)
        db.session.add(voted)
        db.session.commit()

        return redirect('/member/logout')
    else:
        flash("投票過程有問題，停止交易！")
    return render_template('vote.html', form=form, totaluser=totaluser, voteuser=voteuser)


# 投完票直接登出
@member.route('/logout')
@login_required
def logout():
    totaluser = UserRegister.query.count()
    voteuser = UserRegister.query.filter_by(vote=True).count()
    allresult = UserVote.query.count()
    Yesresult = UserVote.query.filter_by(YorN="Y").count()
    Yespercent = (Yesresult/allresult)*100

    logout_user() # flask-login內建的登出函式
    flash('感謝您的參與😊')
    return render_template('flashmessage.html', Yespercent=Yespercent, totaluser=totaluser, voteuser=voteuser)