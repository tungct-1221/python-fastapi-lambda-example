
from time import perf_counter_ns
from uuid import uuid4

from fastapi import Request
from src.core.context import correlation_id_ctx
from src.core.middleware import logger
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp


class CorrelationMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app: ASGIApp,
        header_process_id_name: str = "X-Api-Request-ID",
        header_process_time_name: str = "X-Api-Process-Time",
    ):
        super().__init__(app)
        self.header_request_id_name = header_process_id_name
        self.header_process_time_name = header_process_time_name

    async def dispatch(self, request: Request, call_next):
        apigw_request_id = request.state.lambda_lambda_context.get("request_id")

        host = request.client.host if request.client else "unknown"
        port = request.client.port if request.client else "unknown"
        request_id: str = str(uuid4()) if apigw_request_id is None else apigw_request_id
        start_time = perf_counter_ns()
        correlation_id_ctx.set(request_id)
        logger.info(msg=f'{host}:{port} "{request.method} {request.url}" incoming request')
        response = await call_next(request)
        end_time = perf_counter_ns()
        elapsed_time_ns = end_time - start_time
        elapsed_time_ms = elapsed_time_ns / 1000000
        response.headers[self.header_request_id_name] = request_id
        response.headers[self.header_process_time_name] = f"{elapsed_time_ms:.2f} ms"
        logger.info(
            msg=f'{host}:{port} "{request.method} {request.url}" {response.status_code} {elapsed_time_ms:.2f} ms'
        )
        return response
