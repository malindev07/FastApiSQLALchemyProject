import pyshorteners


def make_short_url(long_url: str):
    short_url: pyshorteners.Shortener = pyshorteners.Shortener().tinyurl.short(long_url)
    return short_url
