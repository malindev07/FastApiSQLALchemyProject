from sqlalchemy import create_engine

from db.db_action import Storage
from db.db_model import Base

engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5432/ShortURLs", echo=False
)

# Base.metadata.create_all(engine)

# my_db = Storage()
# my_db.engine_to_connect = engine
