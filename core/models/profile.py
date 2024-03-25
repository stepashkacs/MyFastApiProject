from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import UserRepresentationMixin




class Profile(UserRepresentationMixin, Base):
    _user_back_populates = 'profile'
    _user_id_unique = True
    first_name: Mapped[str | None] = mapped_column(String(40))
    last_name: Mapped[str | None] = mapped_column(String(40))
    bio: Mapped[str | None]

