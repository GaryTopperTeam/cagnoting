import datetime

from uuid import uuid4
from sqlalchemy import Column, Integer, String, DateTime
from common.db.base import Base


class Movement(Base):
    __tablename__ = 'movement'

    uniqid = Column(String(36),
                    primary_key=True,
                    default=lambda: str(uuid4()))
    value = Column(Integer, nullable=True)
    created_at = Column(DateTime,
                        unique=False,
                        default=datetime.datetime.utcnow)

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return '<Movement %r (%s) at %s>' % (self.value, self.uniqid, self.created_at)
