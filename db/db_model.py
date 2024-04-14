from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


class URLs(Base):
    __tablename__ = "urls"

    id: Mapped[int] = mapped_column(primary_key=True)
    longurl: Mapped[str]
    shorturl: Mapped[str]
