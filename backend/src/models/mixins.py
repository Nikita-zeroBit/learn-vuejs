import uuid

from sqlalchemy import Column
from sqlalchemy_utils import UUIDType


class UuidMixin:
    id = Column(
        UUIDType(binary=False),
        primary_key=True,
        default=uuid.uuid4,
    )
