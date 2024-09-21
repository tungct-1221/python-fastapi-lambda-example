from fastapi import Request
from fastapi.responses import JSONResponse
from src.core.middleware import logger
from starlette.middleware.base import BaseHTTPMiddleware


class ExceptionHandlingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
        except Exception as e:
            logger.exception(e)
            response = JSONResponse(
                status_code=500,
                content={"message": "Oops! Something went wrong!"},
            )
        return response
