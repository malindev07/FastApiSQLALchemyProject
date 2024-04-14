from typing import List

from fastapi import APIRouter, Request

from action_url.url_model import UrlData
from db.db_model import URLs
from db.db_connect import my_db

urls_router = APIRouter(prefix="/short_urls", tags=["Urls"])


@urls_router.get("/items")
def get_items() -> List[UrlData]:
    return my_db.get_items()


@urls_router.get("/item")
def get_item_by_url(url: str) -> UrlData:
    return my_db.get_item(url)


@urls_router.post("/create_item")
def create_short_url(long_url: str) -> UrlData:
    return my_db.create_item(long_url)


@urls_router.delete("/delete_item")
def delete_item(url: str) -> None:
    return my_db.delete_item(url)


@urls_router.put("/update_item")
def update_item(old_url: str, new_url: str) -> UrlData:
    return my_db.update_item(old_url=old_url, new_url=new_url)
