
from logging import getLogger

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.core.exceptions import ForbiddenError
from src.dependencies import get_db
from src.users.models import User
from src.users.schemas import readUserRequest

logger = getLogger(__name__)

user_router = APIRouter(prefix="/users", tags=["users", "v2"])


@user_router.get("")
async def read_users(db: Session = Depends(get_db)):
    # Query example. pls move this to a service and crud
    stmt = select(User)
    for user in db.scalars(stmt):
        user_detail = user.user_detail

        logger.info("user data: " + str(user.id) + " " + str(user.created_at))
        if user_detail:
            logger.info("user detail data: " + str(user_detail.id) + " " + str(user_detail.nickname))

    return {"message": "Get all users"}


@user_router.get("/{user_id}")
async def read_user(user_id: int, payload: readUserRequest):
    if user_id != payload.user_id:
        raise ForbiddenError("User ID is not valid")
    return {"message": f"Get user {user_id}"}
