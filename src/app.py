from fastapi import FastAPI

from src.controller import ping
from src.common.middlewares import TraceMiddleware

# init_log()

app = FastAPI()
app.include_router(ping.router)

app.add_middleware(TraceMiddleware)
