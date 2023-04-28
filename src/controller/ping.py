from logging import getLogger

from fastapi import APIRouter
from pydantic import BaseModel

# from src.common.logger import logger

router = APIRouter()
logger = getLogger("rbac")


class PingResp(BaseModel):
    message: str


@router.get("/ping")
async def ping() -> PingResp:
    logger.info("123")
    return PingResp(message="pong")
