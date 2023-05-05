from uuid import UUID

from schemas.mixins import OrjsonMixin, PaginatedListMixin


class BooksBase(OrjsonMixin):
    title: str
    description: str
    year: str

    class Config:
        orm_mode = True


class BooksCreate(BooksBase):
    pass

class Book(BooksBase):
    id: UUID


class BooksList(PaginatedListMixin):
    results: list[Book] = []

    class Config:
        orm_mode = True
