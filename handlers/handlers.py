from typing import List

from fastapi import APIRouter, Request

from action_url.url_model import UrlData


urls_router = APIRouter(prefix="/short_urls", tags=["Urls"])


@urls_router.get("/items")
def get_items(req: Request) -> List[UrlData]:
    return req.state.storage.get_items()


@urls_router.get("/item")
def get_item_by_url(url: str, req: Request) -> UrlData:
    return req.state.storage.get_item(url)


@urls_router.post("/create_item")
def create_short_url(long_url: str, req: Request) -> UrlData:
    return req.state.storage.create_item(long_url)


@urls_router.delete("/delete_item")
def delete_item(url: str, req: Request) -> None:
    return req.state.storage.delete_item(url)


@urls_router.put("/update_item")
def update_item(old_url: str, new_url: str, req: Request) -> UrlData:
    return req.state.storage.update_item(old_url=old_url, new_url=new_url)
