from fastapi import FastAPI
from database import engine, Base
from models.log import Log
from routers.log_router import router
from middlewares.exception_handler_middleware import ExceptionHandlerMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Huma interview", version="1.0")

app.add_middleware(ExceptionHandlerMiddleware)

app.include_router(router)