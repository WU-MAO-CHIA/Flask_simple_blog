from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_bcrypt import Bcrypt
from flask_login import login_user, logout_user

from apps import app
from config.settings import db
from models.user import User

from .forms import UserLoginForm, UserRegisterForm

user_bp = Blueprint("user", __name__)
bcrypt = Bcrypt(app)

@user_bp.route("/sign_up")
def new() -> str:
    form = UserRegisterForm()
    return render_template("users/new.html.jinja", form=form)

@user_bp.route("/create", methods=["POST"])
def create() -> str:
    form = UserRegisterForm(request.form)
    user = User(username=form.username.data, password = form.password.data)

    if form.validate():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("註冊成功！")
        return redirect(url_for("root"))

    return render_template("users/new.html.jinja", form=form)

@user_bp.route("/login", methods=["POST", "GET"])
def login() -> str:
    form = UserLoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("登入成功")
            return redirect(url_for("root"))
        else:
            flash("帳號或密碼錯誤")

    return render_template("users/login.html.jinja", form=form)

@user_bp.route("/logout", methods=["POST"])
def logout() -> str:
    logout_user()
    flash("已登出")
    return redirect(url_for("root"))
