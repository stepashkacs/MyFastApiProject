from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy import func

from .base import Base

class Order(Base):

    promocode: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.now,
        nullable=True
    )
