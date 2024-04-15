import asyncio
import contextlib
from typing import TypedDict, AsyncIterator

import uvicorn

from fastapi import FastAPI

from db.db_action import Storage
from db.db_connect import engine, async_engine
from handlers.handlers import urls_router


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator:

    try:
        storage = Storage()
        storage.engine_to_connect = engine
        storage.async_engine_connect = async_engine
        yield {"storage": storage}
    finally:
        # storage.connect_close()
        engine.dispose()
        await async_engine.dispose()
        await asyncio.gather()


app = FastAPI(lifespan=lifespan)

app.include_router(urls_router)

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    try:
        uvicorn.run("main:app")

    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    finally:
        print("Exit from app")
    # asyncio.run(lifespan(app))
