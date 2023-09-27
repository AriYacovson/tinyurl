from fastapi import APIRouter

from app.services import redis_service

router = APIRouter(tags=["redis"], prefix="/redis")


@router.get("/get_key")
async def get_key(key: str) -> str:
    return str(redis_service.redis_get(key))


@router.get("set_key")
async def set_key(key: str, value: str) -> bool:
    return redis_service.redis_set(key, value)
