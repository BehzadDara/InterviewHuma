from fastapi import FastAPI
from database import engine, Base
from models.log import Log
from routers.log_router import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Huma interview", version="1.0")

app.include_router(router)