import uuid

from fastapi.openapi.models import Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request

from src.common.context import request_id


class TraceMiddleware(BaseHTTPMiddleware):
    """
    设置全局上下文 request_id
    1. 从请求头中获取 X-Request-ID
    2. 如果没有 X-Request-ID 则生成一个 uuid
    3. 将 request_id 设置到全局上下文中
    """
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        header_request_id = request.headers.get("X-Request-ID")
        if header_request_id:
            request_id.set(header_request_id)
        else:
            request_id.set(str(uuid.uuid1()))
        response = await call_next(request)
        return response
