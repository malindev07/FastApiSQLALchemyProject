from sqlalchemy import Engine, select, or_, delete
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.orm import Session

from action_url.make_short_url import make_short_url
from action_url.url_model import UrlData

from db.db_model import URLs


class Storage:
    engine_to_connect: Engine
    async_engine_connect: AsyncEngine

    async def create_item(self, long_url: str) -> UrlData:
        async with AsyncSession(self.async_engine_connect) as session:
            item = URLs(longurl=long_url, shorturl=make_short_url(long_url))
            session.add(item)
            await session.commit()

            stmt = select(URLs).where(
                or_(URLs.longurl == long_url, URLs.shorturl == long_url)
            )

            for item in await session.scalars(stmt):
                url_data = UrlData(
                    id=item.id, long_url=item.longurl, short_url=item.shorturl
                )

            await self.async_engine_connect.dispose()
            return url_data

    async def get_item(self, url: str) -> UrlData:
        async with AsyncSession(self.async_engine_connect) as session:

            stmt = select(URLs).where(or_(URLs.longurl == url, URLs.shorturl == url))

            for item in await session.scalars(stmt):
                url_data = UrlData(
                    id=item.id, long_url=item.longurl, short_url=item.shorturl
                )

                await self.async_engine_connect.dispose()
                return url_data

    async def get_items(self) -> [UrlData]:
        async with AsyncSession(self.async_engine_connect) as session:

            stmt = select(URLs)
            urls_arr: [UrlData] = []

            for item in await session.scalars(stmt):
                urls_arr.append(
                    UrlData(id=item.id, long_url=item.longurl, short_url=item.shorturl)
                )
            await self.async_engine_connect.dispose()
            return urls_arr

    async def delete_item(self, url: str) -> None:
        async with AsyncSession(self.async_engine_connect) as session:
            stmt = delete(URLs).where(
                or_(URLs.longurl.like(url), URLs.shorturl.like(url))
            )
            await session.execute(stmt)
            await session.commit()
            await self.async_engine_connect.dispose()

    async def update_item(self, old_url: str, new_url: str) -> UrlData:
        async with AsyncSession(self.async_engine_connect) as session:
            stmt = select(URLs).where(URLs.longurl == old_url)
            for item in await session.scalars(stmt):
                item.longurl = new_url
                item.shorturl = make_short_url(new_url)
                url_data = UrlData(
                    id=item.id, long_url=item.longurl, short_url=item.shorturl
                )

            await session.commit()
            await self.async_engine_connect.dispose()
            return url_data

    # def connect_close(self):
    #     with Session(self.engine_to_connect) as session:
    #         session.close()
