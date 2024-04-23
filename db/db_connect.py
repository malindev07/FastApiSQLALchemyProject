from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine

# engine = create_engine(
#     "postgresql+psycopg2://postgres:postgres@localhost:5432/ShortURLs", echo=False
# )

# async_engine = create_async_engine(
#     "postgresql+asyncpg://postgres:postgres@localhost:5432/ShortURLs", echo=False
# )


def db_connect(driver: str, login: str, password: str) -> AsyncEngine:
    async_engine: AsyncEngine = create_async_engine(
        f"postgresql+{driver}://{login}:{password}@localhost:5432/ShortURLs",
        echo=False,
    )
    return async_engine
