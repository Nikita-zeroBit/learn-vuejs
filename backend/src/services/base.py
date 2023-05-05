from http import HTTPStatus
from typing import TypeVar
from uuid import UUID

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from core.messages import RECORD_NOT_FOUND
from schemas.mixins import OrjsonMixin, PaginatedListMixin
from services.utils import compute_page_numbers


DEFAULT_PAGE_SIZE = 20


Record = TypeVar('Record', bound=OrjsonMixin)


class BaseService:
    _model = None
    _paginated_response_model = PaginatedListMixin

    def __init__(self, db):
        self.db = db

    @property
    def model(self):
        if self._model is None:
            raise NotImplementedError('Please, set _model property!')
        return self._model

    @property
    def paginated_model(self):
        if self._paginated_response_model is None:
            raise NotImplementedError('Please, set _paginated_response_model property!')
        return self._paginated_response_model

    def get_by_id(self, rec_id: UUID):
        query = self.db.query(self.model).filter(self.model.id == rec_id)
        record = query.first()
        if record is None:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=RECORD_NOT_FOUND)
        return record

    def get_list(self, order_by: str = 'id') -> list[Record]:
        query = self.db.query(self.model)
        order = getattr(self.model, order_by)
        return query.order_by(order).all()

    def paginate_result(self, query, page_number: int = 1, page_size: int = DEFAULT_PAGE_SIZE):
        records = query.limit(page_size).offset((page_number - 1) * page_size).all()
        total = query.count()

        data = compute_page_numbers(current_page=page_number, records_per_page=page_size, total_records=total)
        data['results'] = records

        result = self.paginated_model.parse_obj(data)
        return result

    def get_list_paginated(self, page_number: int = 1, page_size: int = DEFAULT_PAGE_SIZE):
        query = self.db.query(self.model)
        return self.paginate_result(query=query, page_number=page_number, page_size=page_size)

    def create(self, data: Record):
        try:
            record = self.model(**data.dict())
            self.db.add(record)
            self.db.commit()
        except (IntegrityError, ValueError) as e:
            raise HTTPException(status_code=HTTPStatus.CONFLICT, detail=e.args)
        return record

    def update(self, rec_id: int, data: Record):
        query = self.db.query(self.model).filter(self.model.id == rec_id)
        record = query.first()
        for key, val in data.dict().items():
            setattr(record, key, val)
        self.db.add(record)
        self.db.commit()
        return record
    
    def delete(self, rec_id: int):
        query = self.db.query(self.model).filter(self.model.id == rec_id)
        record = query.first()
        self.db.delete(record)
        self.db.commit()
        return "OK"
