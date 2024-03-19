from pydantic import BaseModel
from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / 'db.sqlite3'

class BdSetting(BaseModel):
    url: str = f"sqlite+aiosqlite:///{DB_PATH}"  # Используем путь к базе данных
    echo: bool = True
class Setting(BaseSettings):
    db: BdSetting = BdSetting()
    api_v1_prefix: str = '/api/v1'
setting = Setting()
