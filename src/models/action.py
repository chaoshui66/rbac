from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Action(DeclarativeBase):
    __tablename__ = "action"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    resource_id: Mapped[int] = mapped_column()
    region_name: Mapped[str] = mapped_column()
    created_at: Mapped[int] = mapped_column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    updated_at: Mapped[int] = mapped_column(TIMESTAMP, server_default="CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
