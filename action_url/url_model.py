from dataclasses import dataclass
from typing import Optional


@dataclass
class UrlData:
    id: Optional[int] | None
    long_url: str
    short_url: str
