
from typing import AsyncIterator

from sqlalchemy.orm import Session
from src.core.database import sessionmanager


def get_db():
    session = sessionmanager.get_session()
    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
