from db.database import get_db_connector
from models.user import User
from services.base import BaseService


def get_users_service():
    return UsersService(get_db_connector())


class UsersService(BaseService):
    _model = User
