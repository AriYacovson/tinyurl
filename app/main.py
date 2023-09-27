from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

from app.routers import redis_controller

app = FastAPI()

app.include_router(router=redis_controller.router)
