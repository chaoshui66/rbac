from contextvars import ContextVar

# 全局请求上下文
request_id: ContextVar[str] = ContextVar("request_id", default="unknown")
