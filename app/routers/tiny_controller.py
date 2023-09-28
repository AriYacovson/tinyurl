from fastapi import APIRouter

from app.schemas.new_tiny_request import NewTinyRequest
from app.services.tiny_service import new_tiny


router = APIRouter(tags=["tiny"], prefix="/tiny")


@router.post("/")
async def create_new_tiny(new_tiny_request: NewTinyRequest):
    return new_tiny(new_tiny_request.url)
