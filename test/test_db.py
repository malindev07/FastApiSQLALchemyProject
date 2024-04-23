from action_url.make_short_url import make_short_url
from db.db_connect import db_connect


def test_db():
    db = db_connect(driver="asyncpg", login="postgres", password="postgres")
    assert str(db.url) == "postgresql+asyncpg://postgres:***@localhost:5432/ShortURLs"


def test_short_url():
    assert isinstance(make_short_url(long_url="https://www.hltv.org/"), str)
