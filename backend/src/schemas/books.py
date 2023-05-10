from uuid import UUID
from typing import List

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
    results: List[Book] = []

    class Config:
        orm_mode = True
