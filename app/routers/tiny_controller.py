from fastapi import APIRouter

from app.schemas.new_tiny_request import NewTinyRequest
from app.services.tiny_service import new_tiny, get_tiny



router = APIRouter(tags=["tiny"], prefix="/tiny")


@router.post("/")
async def create_new_tiny(new_tiny_request: NewTinyRequest):
    return new_tiny(new_tiny_request.url)


@router.get("/{tiny_url}")
async def get_tinyurl(tiny_url: str):
    tiny = get_tiny(tiny_url)
    if tiny:
        return "redirect:" + tiny
    else:
        raise Exception(tiny + "NOT FOUND")
