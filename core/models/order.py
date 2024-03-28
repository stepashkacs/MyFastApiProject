from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import func

from .base import Base
from .order_product_association import order_product_association_table

if TYPE_CHECKING:
    from .product import Product


class Order(Base):

    promocode: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.now,
        nullable=True
    )
    products: Mapped[list['Product']] = relationship(
        secondary=order_product_association_table,
        back_populates='orders',
    )
