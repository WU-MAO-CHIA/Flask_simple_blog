from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func

from config.settings import db


class Post(db.Model):
    __tablename__ = "posts"

    def __repr__(self) -> str:
        return f"{self.title}"

    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String, nullable=False)
    content = mapped_column(Text, nullable=True)
    created_at = mapped_column(DateTime, server_default=func.now())
    updated_at = mapped_column(DateTime, server_default=func.now())
