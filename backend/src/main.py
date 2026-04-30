import os
from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.db import init_db
from api.chat.routing import router as chat_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # before app startup
    init_db()
    yield
    # after app startup
    
app = FastAPI(lifespan=lifespan)
app.include_router(chat_router, prefix="/api/chats")
# the or acts as a fallback in case the environment variable is not set, it will use the default value instead
MY_PROJ = os.environ.get("MY_PROJ") or "default_proj"
API_KEY = os.environ.get("API_KEY")

if not API_KEY:
    raise NotImplementedError("API_KEY environment variable is not set")

@app.get("/")
def read_index():
    return {"Hello": "World", "project-name": MY_PROJ}