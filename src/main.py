

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.core.database import sessionmanager
from src.core.logger import configure_logging
from src.core.middleware.context_middleware import ContextMiddleware
from src.core.middleware.correlation_middleware import CorrelationMiddleware
from src.core.middleware.exception_handle_middleware import ExceptionHandlingMiddleware
from src.routers.v2 import v2_router

app = FastAPI(on_startup=[configure_logging])


# Add middleware
# Please note that the order of middleware is important
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(ExceptionHandlingMiddleware)
app.add_middleware(CorrelationMiddleware)
app.add_middleware(ContextMiddleware)

# init DB
sessionmanager.init_db()

# Add routers
app.include_router(v2_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Example API"}


@app.get("/health")
def read_health():
    return {"status": "UP"}
