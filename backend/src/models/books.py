from sqlalchemy import Column, String, Integer

from models.mixins import UuidMixin


from db.database import Base


class Book(Base, UuidMixin):
    __tablename__ = 'books'

    title = Column(String, index=True, nullable=False)
    description = Column(String, index=True, nullable=False, unique=True)
    year = Column(Integer, index=True)
