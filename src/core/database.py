
from sqlalchemy import URL, Engine, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from src.core.config import settings

database_url = URL.create(
    "postgresql+psycopg",
    username=settings.DATABASE_USER,
    password=settings.DATABASE_PASSWORD,  # plain (unescaped) text
    host=settings.DATABASE_HOST,
    database=settings.DATABASE_NAME,
)


class Base(DeclarativeBase):
    pass


class DatabaseSessionManager:
    def __init__(self):
        self.engine: Engine | None = None
        self.session_maker = None

        # self.async_engine: AsyncEngine | None = None
        # self.async_session_maker = None

    def init_db(self):
        # Database connection parameters...

        # Creating synchronous and asynchronous engines
        # self.async_engine = create_async_engine(database_url, pool_size=1, max_overflow=0, pool_pre_ping=False)
        self.engine = create_engine(database_url, pool_size=1, max_overflow=0, pool_pre_ping=False)

        # Creating an asynchronous session class
        # self.async_session_maker = async_sessionmaker(autocommit=False, autoflush=False, bind=self.async_engine)

        # Creating a scoped session
        # self.session = async_scoped_session(self.session_maker, scopefunc=current_task)
        self.session_maker = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    # def get_async_session(self):
    #     if self.async_session_maker is None:
    #         raise Exception("DatabaseSessionManager is not initialized")
    #     return self.async_session_maker()

    def get_session(self):
        if self.session_maker is None:
            raise Exception("DatabaseSessionManager is not initialized")
        return self.session_maker()

    # def close(self):
    #     # Closing the database session...
    #     if self.engine is None:
    #         raise Exception("DatabaseSessionManager is not initialized")
    #     self.engine.dispose()


# Initialize the DatabaseSessionManager
sessionmanager = DatabaseSessionManager()
