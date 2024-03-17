from sqlalchemy.orm import DeclarativeBase, relationship, mapped_column, Mapped, declared_attr


class Base(DeclarativeBase):
    __abstract__ = True #Говорит о том что это моделать не будет в базе данных

    @declared_attr.directive #Делает таблицы с именем меделей добовляя 's в конце
    def __tablename__(cls) -> str:
        return f'{cls.__name__.lower()}s'

    id: Mapped[int] = mapped_column(primary_key=True)

