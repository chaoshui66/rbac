from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import TIMESTAMP


class Region(DeclarativeBase):
    __tablename__ = "region"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[int] = mapped_column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    updated_at: Mapped[int] = mapped_column(TIMESTAMP, server_default="CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
