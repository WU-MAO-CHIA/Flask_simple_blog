from flask_login import UserMixin
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, relationship

from config.settings import db

from .mixnis.datetime import TimeTrackable

# class UserMixin:
#     def is_active(self) -> bool:
#         return True

#     def is_authenticated(self) -> bool:
#         return True
    
#     def get_id(self) -> str:
#         return str(self.id)


class User(db.Model, TimeTrackable, UserMixin):
    __tablename__ = "users"

    def __repr__(self) -> str:
        return f"{self.username}"

    id = mapped_column(Integer, primary_key=True)
    username = mapped_column(String(50), nullable=False)
    password = mapped_column(String(100), nullable=False)

    posts = relationship("Post", back_populates="auther")