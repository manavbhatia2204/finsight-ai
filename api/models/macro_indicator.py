from datetime import date

from sqlalchemy import Date, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from api.models.base import Base


class MacroIndicator(Base):
    __tablename__ = "macro_indicators"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    indicator_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    indicator_code: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    value: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )