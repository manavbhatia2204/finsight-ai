from datetime import date

from sqlalchemy import BigInteger, Date, Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from api.models.base import Base


class StockPrice(Base):
    __tablename__ = "stock_prices"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    stock_id: Mapped[int] = mapped_column(
        ForeignKey("stocks.id"),
        nullable=False
    )

    date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    open: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    high: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    low: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    close: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    volume: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False
    )