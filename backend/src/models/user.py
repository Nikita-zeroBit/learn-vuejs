from sqlalchemy import Column, String

from models.mixins import UuidMixin


from db.database import Base


class User(Base, UuidMixin):
    __tablename__ = 'users'

    name = Column(String, index=True, nullable=False)
    email = Column(String, index=True, nullable=False, unique=True)
    password = Column(String, nullable=False)
