from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Access(DeclarativeBase):
    __tablename__ = "access"

    id: Mapped[int] = mapped_column(primary_key=True)
    role_id: Mapped[str] = mapped_column()
    uid: Mapped[str] = mapped_column()
    action_id: Mapped[int] = mapped_column()
    created_at: Mapped[int] = mapped_column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    updated_at: Mapped[int] = mapped_column(TIMESTAMP, server_default="CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
