# wtform建立各種需要的Form

from flask_wtf import FlaskForm # Flask表單
from wtforms import StringField, SubmitField, validators, EmailField, ValidationError, BooleanField, RadioField

# 註冊登錄用的form
class FormRegister(FlaskForm):
    username = StringField('暱稱', render_kw={'class':'searchtext', 'placeholder': '暱稱'}, validators=[
        validators.DataRequired()
    ])
    email = EmailField('公司信箱', render_kw={'class':'searchtext', 'placeholder':  '請輸入公司信箱'}, validators=[
        validators.DataRequired()
    ])

    vote = BooleanField('已投票')

    submit = SubmitField('登錄名單', render_kw={'class':'btn btn-outline-secondary'})


# 登入投票 (以email為主要登入帳號)
class FormLogin(FlaskForm):
    email = EmailField('公司信箱', render_kw={'class':'searchtext', 'placeholder': '請輸入您的公司信箱'}, validators=[
        validators.DataRequired()
    ])

    submit = SubmitField('投票去 👉', render_kw={'class':'btn btn-outline-secondary'})

# 投票用
class FormVote(FlaskForm):
    YorN = RadioField('是否願意支持茜渝留下來服務大家？', choices=[('Y', '願意啦哪次不願意👌'), ('N', '然而我拒絕（茜渝：嗚嗚再考慮一下嘛😭）')],  validators=[
        validators.DataRequired()])

    submit = SubmitField('我決定好了(❁´◡`❁)', render_kw={'class':'btn btn-outline-secondary'})