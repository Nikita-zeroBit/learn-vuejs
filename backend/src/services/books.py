from db.database import get_db_connector
from models.books import Book
from services.base import BaseService


def get_books_service():
    return BooksService(get_db_connector())


class BooksService(BaseService):
    _model = Book
