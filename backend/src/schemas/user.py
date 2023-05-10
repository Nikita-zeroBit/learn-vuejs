from uuid import UUID
from typing import List

from schemas.mixins import OrjsonMixin, PaginatedListMixin


class UserBase(OrjsonMixin):
    email: str
    name: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: UUID
    password: str


class UserList(PaginatedListMixin):
    results: List[User] = []

    class Config:
        orm_mode = True
