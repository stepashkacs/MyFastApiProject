from fastapi import FastAPI
from contextlib import asynccontextmanager

from core.models import Base, db_helper
from users.views import router as users_router
from api_v1 import router as router_v1
from core.config import setting
@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(users_router)
app.include_router(router_v1, prefix=setting.api_v1_prefix)