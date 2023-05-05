from uuid import UUID

from fastapi import APIRouter, Depends

from schemas.mixins import PaginatedParams
from schemas.books import BooksCreate, Book, BooksList
from services.books import BooksService, get_books_service

router = APIRouter()


@router.get('/', response_model=BooksList,
            summary='Show books',
            description='Show list of books')
def get_users(service: BooksService = Depends(get_books_service),
              page_params: PaginatedParams = Depends()) -> BooksList:
    return service.get_list_paginated(**page_params.dict())


@router.post('/',
             summary='Create book',
             description='Create book object')
def create_user(book: BooksCreate,
                service: BooksService = Depends(get_books_service)):
    return service.create(data=book)


@router.get('/{book_id}', response_model=Book,
            summary='Show book by id',
            description='Show selected book')
def get_user(book_id: UUID,
             service: BooksService = Depends(get_books_service)) -> Book:
    return service.get_by_id(rec_id=book_id)

@router.delete('/{book_id}',
                summary='Delete book',
                description='Delete selected book')
def get_user(book_id: UUID, service: BooksService = Depends(get_books_service)) -> str:
    return service.delete(rec_id=book_id)
