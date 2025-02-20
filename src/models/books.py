from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.database import Base


class BookModel(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[str]
