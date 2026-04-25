import os
from dotenv  import load_dotenv
from pathlib import Path
from flask import Flask

load_dotenv()

ROOT_PATH = Path().absolute()
TEMPLAGE_FOLDER  = ROOT_PATH / "templates"
DB_PATH = ROOT_PATH / "db" / "blog.db"

app = Flask(__name__, template_folder = TEMPLAGE_FOLDER )
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.secret_key = os.getenv("APP_SECRET_KEY")