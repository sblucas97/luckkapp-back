import uuid
from luckapp.database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean

class User(Base):
    # """Model for user accounts."""
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    full_name = Column(String(64), unique=False, nullable=False)
    city = Column(String(80), unique=False, nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    phone = Column(String(14), unique=False, nullable=False)
    password = Column(String(18), unique=False, nullable=True)
    is_admin = Column(Boolean, unique=False, nullable=False)
    birthday = Column(DateTime, unique=False, nullable=False)
    updated_at = Column(DateTime, unique=False, nullable=False)
    created_at = Column(DateTime, unique=False, nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.full_name)