from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from core.config import setting

class DatabaseHelper:
    def __init__(self, url: str, echo: bool = True):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

db_helper = DatabaseHelper(
    url=setting.db.url,
    echo=setting.db.echo,
)
