import os

from dotenv import load_dotenv
from fastapi import FastAPI

from app.routers import tiny_controller

load_dotenv(".env")
# a = os.environ.get("BASE_URL")
# print(a)

app = FastAPI()

app.include_router(tiny_controller.router)
