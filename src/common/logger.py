import logging
from copy import copy

from uvicorn.logging import AccessFormatter, DefaultFormatter

from src.common.context import request_id


class WithRequestIdMixin:

    def formatMessage(self, record: logging.LogRecord) -> str:  # noqa
        record_copy = copy(record)
        record_copy.__dict__.update(
            {
                "trace_id": request_id.get()
            }
        )
        return super().formatMessage(record_copy) # noqa


# 为 uvicorn 的日志加上 trace_id 字段
class CustomUvicornAccessFormatter(WithRequestIdMixin, AccessFormatter):
    pass


class RawFormatter(WithRequestIdMixin, DefaultFormatter):
    pass


log_conf = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "raw_formatter": {
            "class": "logging.Formatter",
            "format": "%(asctime)s - %(levelname)s:     %(filename)s:%(lineno)d - %(message)s"
        }
    },
    "handlers": {
        "console_handler": {
            "formatter": "raw_formatter",
            "class": "logging.StreamHandler"
        }
    },
    "loggers": {
        "rbac": {
            "handlers": ["console_handler"],
            "level": "INFO",
            "propagate": False
        }
    }
}

logging.config.dictConfig(log_conf)
