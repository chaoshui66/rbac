from sqlalchemy import TIMESTAMP
from sqlalchemy import JSON
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class User(DeclarativeBase):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    uid: Mapped[str] = mapped_column(unique=True)
    region_name: Mapped[str] = mapped_column()
    uname: Mapped[str] = mapped_column()
    role_id_list: Mapped[list[str]] = mapped_column(JSON)
    hashed_password: Mapped[str] = mapped_column()
    created_at: Mapped[int] = mapped_column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    updated_at: Mapped[int] = mapped_column(TIMESTAMP, server_default="CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
