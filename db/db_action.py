from sqlalchemy import Engine, select, or_, delete
from sqlalchemy.orm import Session

from action_url.make_short_url import make_short_url
from action_url.url_model import UrlData


from db.db_model import URLs


class Storage:
    engine_to_connect: Engine

    # def set_connect(self):
    #     self.engine_to_connect = engine

    def create_item(self, long_url: str) -> UrlData:
        with Session(self.engine_to_connect) as session:
            item = URLs(longurl=long_url, shorturl=make_short_url(long_url))
            session.add(item)
            session.commit()

            stmt = select(URLs).where(
                or_(URLs.longurl == long_url, URLs.shorturl == long_url)
            )

            for item in session.scalars(stmt):
                url_data = UrlData(
                    id=item.id, long_url=item.longurl, short_url=item.shorturl
                )

            return url_data

    def get_item(self, url: str) -> UrlData:
        with Session(self.engine_to_connect) as session:

            stmt = select(URLs).where(or_(URLs.longurl == url, URLs.shorturl == url))

            for item in session.scalars(stmt):
                url_data = UrlData(
                    id=item.id, long_url=item.longurl, short_url=item.shorturl
                )

                return url_data

    def get_items(self) -> [UrlData]:
        with Session(self.engine_to_connect) as session:

            stmt = select(URLs)
            urls_arr: [UrlData] = []

            for item in session.scalars(stmt).all():
                urls_arr.append(
                    UrlData(id=item.id, long_url=item.longurl, short_url=item.shorturl)
                )

            return urls_arr

    def delete_item(self, url: str) -> None:
        with Session(self.engine_to_connect) as session:
            stmt = delete(URLs).where(
                or_(URLs.longurl.like(url), URLs.shorturl.like(url))
            )
            session.execute(stmt)
            session.commit()

    def update_item(self, old_url: str, new_url: str) -> UrlData:
        with Session(self.engine_to_connect) as session:
            stmt = select(URLs).where(URLs.longurl == old_url)
            for item in session.scalars(stmt):
                item.longurl = new_url
                item.shorturl = make_short_url(new_url)
                url_data = UrlData(
                    id=item.id, long_url=item.longurl, short_url=item.shorturl
                )

            session.commit()

            return url_data

    # def connect_close(self):
    #     with Session(self.engine_to_connect) as session:
    #         session.close()
