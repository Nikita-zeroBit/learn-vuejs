from uuid import UUID

from fastapi import APIRouter, Depends

from schemas.mixins import PaginatedParams
from schemas.user import UserCreate, User, UserList
from services.users import UsersService, get_users_service

router = APIRouter()


@router.get('/', response_model=UserList,
            summary='Show users',
            description='Show list of users')
def get_users(service: UsersService = Depends(get_users_service),
              page_params: PaginatedParams = Depends()) -> UserList:
    return service.get_list_paginated(**page_params.dict())


@router.post('/',
             summary='Create user',
             description='Create user object')
def create_user(user: UserCreate,
                service: UsersService = Depends(get_users_service)):
    return service.create(data=user)

# @router.put('/{user_id}',
#             response_model=User,
#             summary='Update user',
#             description='Update user object')
# def create_user(user_id: UUID,
#                 service: UsersService = Depends(get_users_service)) -> User:
#     return service.update(data=user)


@router.get('/{user_id}',
            response_model=User,
            summary='Show user',
            description='Show selected user')
def get_user(user_id: UUID, service: UsersService = Depends(get_users_service)) -> User:
    return service.get_by_id(rec_id=user_id)


@router.delete('/{user_id}',
                summary='Deelte user',
                description='Delete selected user')
def get_user(user_id: UUID, service: UsersService = Depends(get_users_service)) -> str:
    return service.delete(rec_id=user_id)
