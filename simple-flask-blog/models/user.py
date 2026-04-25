from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column

from config.settings import db

from .mixnis.datetime import TimeTrackable


class User(db.Model, TimeTrackable):
    __tablename__ = "users"

    def __repr__(self) -> str:
        return f"{self.username}"

    id = mapped_column(Integer, primary_key=True)
    username = mapped_column(String(50), nullable=False)
    password = mapped_column(String(100), nullable=False)