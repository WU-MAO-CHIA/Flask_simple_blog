from flask_wtf import Form
from wtforms import PasswordField, StringField
from wtforms.validators import EqualTo, InputRequired, Length, ValidationError
from models.user import User

STYLES = "text-xl w-full md:w-1/2 px-3 py-2 border border-gray-900 rounded-sm"

def unique_username(form, field):
    if User.query.filter_by(username=field.data).first():
        raise ValidationError("該帳號已註冊")

class UserRegisterForm(Form):
    username = StringField(
        "帳號",
        validators = [InputRequired(), Length(min=4, max=20), unique_username],
        render_kw = {"placeholder" : "使用者帳號", "class" : STYLES}
    )
    password = PasswordField(
        "密碼",
        validators = [InputRequired()],
        render_kw = {"placeholder" : "請填寫登入密碼", "class" : STYLES}
    )
    password_confirm = PasswordField(
        "密碼確認",
        validators = [InputRequired(), EqualTo("password", message="密碼確認不符")],
        render_kw = {"placeholder" : "再次確認密碼", "class" : STYLES}
    )
