from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

# from db.db_action import Storage
# from db.db_model import Base

engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5432/ShortURLs", echo=False
)

async_engine = create_async_engine(
    "postgresql+asyncpg://postgres:postgres@localhost:5432/ShortURLs", echo=False
)

async_session = async_sessionmaker(async_engine)

# Base.metadata.create_all(engine)

# my_db = Storage()
# my_db.engine_to_connect = engine
