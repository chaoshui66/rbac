from logging import getLogger

from fastapi import HTTPException
from starlette.requests import Request

from src.common.context import request_id

logger = getLogger("app")


async def un_catch_error_handler(request: Request, exc: Exception):
    """
    全局异常处理
    """
    if isinstance(exc, HTTPException):
        raise
    logger.exception(f"request_id: {request_id.get()} 未捕获的异常: {exc}")
    raise HTTPException(
        status_code=500,
        detail="Internal Server Error"
    )
