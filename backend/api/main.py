from fastapi import FastAPI
import time
from sqlalchemy import text, create_engine

from routers import videos, web

app = FastAPI()

app.include_router(videos.router)
app.include_router(web.router)