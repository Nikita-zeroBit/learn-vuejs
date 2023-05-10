import orjson
from fastapi import Query
from pydantic import BaseModel
from typing import Union


DEFAULT_PAGE_SIZE = 10


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class OrjsonMixin(BaseModel):
    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps


class PaginatedParams(OrjsonMixin):
    page_size: int = Query(DEFAULT_PAGE_SIZE, description='Page size', ge=1)
    page_number: int = Query(1, description='Page number', ge=1)


class PaginatedListMixin(OrjsonMixin):
    prev: Union[int, None]
    next: Union[int, None]
    first: Union[int, None]
    last: Union[int, None]
    results: list  # list of objects
