"""Structured Logging Configuration with Request ID correlation."""

import logging
import sys
from typing import Any, Dict


class StructuredFormatter(logging.Formatter):
    """Formats log records as structured text with request context."""
    def format(self, record: logging.LogRecord) -> str:
        req_id = getattr(record, "request_id", "system")
        base = f"[{self.formatTime(record, self.datefmt)}] [{record.levelname}] [req_id={req_id}] {record.getMessage()}"
        if record.exc_info:
            base += "\n" + self.formatException(record.exc_info)
        return base


def setup_logging(level: str = "INFO") -> logging.Logger:
    logger = logging.getLogger("insurix")
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))
    logger.handlers.clear()

    handler = logging.StreamHandler(sys.stdout)
    formatter = StructuredFormatter(datefmt="%Y-%m-%d %H:%M:%S")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


logger = setup_logging()
