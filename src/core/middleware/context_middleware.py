from json import loads

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp


class ContextMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        lambda_request_context = request.headers.get("x-amzn-request-context")
        lambda_lambda_context = request.headers.get("x-amzn-lambda-context")
        request.state.lambda_request_context = loads(lambda_request_context) if lambda_request_context else {}
        request.state.lambda_lambda_context = loads(lambda_lambda_context) if lambda_lambda_context else {}
        response = await call_next(request)
        return response
