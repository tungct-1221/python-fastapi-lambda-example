
from datetime import date, datetime
from typing import Optional
from uuid import UUID

from sqlalchemy import Date, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.core.database import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "users"}

    id: Mapped[UUID] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    user_detail: Mapped[Optional["UserDetail"]] = relationship(back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(id={self.id!r}, created_at={self.created_at!r})>"


class Gender(Base):
    __tablename__ = "genders"
    __table_args__ = {"schema": "users"}

    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128))

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

class UserDetail(Base):
    __tablename__ = "user_details"
    __table_args__ = {"schema": "users"}

    id: Mapped[UUID] = mapped_column(ForeignKey("users.users.id"), primary_key=True)
    gender_id: Mapped[str] = mapped_column(ForeignKey("users.genders.id"))

    nickname: Mapped[str] = mapped_column(String(255))
    birth_date: Mapped[date] = mapped_column(Date)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    user: Mapped["User"] = relationship(back_populates="user_detail")
