import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager

from models.user import User
from config.settings import db

load_dotenv()

ROOT_PATH = Path().absolute()
# ROOT_PATH = Path(__file__).resolve().parents[2]
TEMPLATE_FOLDER  = ROOT_PATH / "templates"
DB_PATH = ROOT_PATH / "db" / "blog.db"

app = Flask(__name__, template_folder = TEMPLATE_FOLDER )
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.secret_key = os.getenv("APP_SECRET_KEY")
# app.secret_key = "dev-secret-key"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view  = "user.login"
login_manager.login_message = "請登入會員帳號"

@login_manager.user_loader
def load_user(id) -> User:
    return db.session.get(User, int(id))
    # return User.query.get(int(id))