"""Insurix Standardized Error Envelope and Exception Hierarchy."""

from typing import Any, Optional
from fastapi import Request
from fastapi.responses import JSONResponse


class InsurixError(Exception):
    """Base application exception enforcing standard error envelope."""
    def __init__(
        self,
        code: str,
        message: str,
        status_code: int = 400,
        details: Optional[Any] = None
    ):
        super().__init__(message)
        self.code = code
        self.message = message
        self.status_code = status_code
        self.details = details

    def to_dict(self) -> dict:
        return {
            "error": {
                "code": self.code,
                "message": self.message,
                "details": self.details
            }
        }


class ValidationError(InsurixError):
    def __init__(self, message: str, details: Optional[Any] = None):
        super().__init__(code="VALIDATION", message=message, status_code=422, details=details)


class NotFoundError(InsurixError):
    def __init__(self, message: str, details: Optional[Any] = None):
        super().__init__(code="NOT_FOUND", message=message, status_code=404, details=details)


class PayloadTooLargeError(InsurixError):
    def __init__(self, message: str = "File size exceeds 10 MB limit", details: Optional[Any] = None):
        super().__init__(code="PAYLOAD_TOO_LARGE", message=message, status_code=413, details=details)


class UnsupportedMediaError(InsurixError):
    def __init__(self, message: str = "Only PDF documents (%PDF header) are accepted", details: Optional[Any] = None):
        super().__init__(code="UNSUPPORTED_MEDIA", message=message, status_code=415, details=details)


class EngineError(InsurixError):
    def __init__(self, message: str, details: Optional[Any] = None):
        super().__init__(code="ENGINE_ERROR", message=message, status_code=500, details=details)


class LLMUnavailableError(InsurixError):
    def __init__(self, message: str = "LLM synthesis unavailable; fallback active", details: Optional[Any] = None):
        super().__init__(code="LLM_UNAVAILABLE", message=message, status_code=503, details=details)


async def insurix_exception_handler(request: Request, exc: InsurixError) -> JSONResponse:
    return JSONResponse(status_code=exc.status_code, content=exc.to_dict())
