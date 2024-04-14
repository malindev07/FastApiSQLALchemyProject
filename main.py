import uvicorn

from fastapi import FastAPI
from handlers.handlers import urls_router

app = FastAPI()

app.include_router(urls_router)

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
