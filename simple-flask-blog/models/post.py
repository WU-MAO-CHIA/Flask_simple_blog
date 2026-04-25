from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import mapped_column, relationship

from config.settings import db

from .mixnis.datetime import TimeTrackable


class Post(db.Model, TimeTrackable):
    __tablename__ = "posts"

    def __repr__(self) -> str:
        return f"{self.title}"

    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String, nullable=False)
    content = mapped_column(Text, nullable=True)
    user_id = mapped_column(
        Integer, ForeignKey("users.id", name="fk_posts_to_user_id"), nullable=True
    )
    auther = relationship("User", foreign_keys=user_id, back_populates="posts")
