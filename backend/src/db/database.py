from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.config import settings


SQLALCHEMY_DATABASE_URL = (f'postgresql://{settings.postgres_user}:{settings.postgres_password}'
                           f'@{settings.postgres_host}:{settings.postgres_port}/{settings.postgres_db}')


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


db_connector = None


def get_db_connector() -> SessionLocal:
    if db_connector is None:
        raise ValueError('DB connector is not set')
    return db_connector
