
"""
exceptions.py

This module contains global exception classes for the application.
"""

from starlette.exceptions import HTTPException as StarletteHTTPException


class BadRequestError(StarletteHTTPException):
    """Raised when a request is malformed"""

    def __init__(self, detail: str | None = None, headers: dict[str, str] | None = None):
        super().__init__(400, detail, headers)


class NotFoundError(StarletteHTTPException):
    """Raised when a requested resource is not found"""

    def __init__(self, detail: str | None = None, headers: dict[str, str] | None = None):
        super().__init__(404, detail, headers)


class ForbiddenError(StarletteHTTPException):
    """Raised when a user is not authorized to access a resource"""

    def __init__(self, detail: str | None = None, headers: dict[str, str] | None = None):
        super().__init__(403, detail, headers)
