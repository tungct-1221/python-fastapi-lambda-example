
from fastapi import APIRouter

from .users import user_router

v2_router = APIRouter(prefix="/v2", tags=["v2"])

v2_router.include_router(user_router)
