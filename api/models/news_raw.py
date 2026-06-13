from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from api.models.base import Base


class NewsRaw(Base):
    __tablename__ = "news_raw"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    ticker: Mapped[str] = mapped_column(
        String(10),
        nullable=False
    )

    title: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )

    source: Mapped[str] = mapped_column(
        String(100),
        nullable=True
    )

    published_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )

    article_text: Mapped[str] = mapped_column(
        Text,
        nullable=True
    )

    url: Mapped[str] = mapped_column(
        String(1000),
        nullable=True
    )