import asyncio
import contextlib
from typing import TypedDict, AsyncIterator

import uvicorn

from fastapi import FastAPI

from db.db_action import Storage
from db.db_connect import engine
from handlers.handlers import urls_router


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator:

    try:
        storage = Storage()
        storage.engine_to_connect = engine
        yield {"storage": storage}
    finally:
        # storage.connect_close()
        print("Exit from app")


app = FastAPI(lifespan=lifespan)

app.include_router(urls_router)

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    uvicorn.run("main:app")
