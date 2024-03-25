from typing import TYPE_CHECKING
from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import UserRepresentationMixin

if TYPE_CHECKING:
    from .user import User


class Post(UserRepresentationMixin, Base):
    _user_back_populates = 'posts'
    title: Mapped[str] = mapped_column(String(64))
    body: Mapped[str] = mapped_column(
        Text,
        default='',
        server_default='',
    )
