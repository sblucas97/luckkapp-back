import uuid
from luckapp.database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, LargeBinary

class Prize(Base):
    # """Model for user accounts."""
    __tablename__ = 'prizes'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String(64), unique=False, nullable=False)
    description = Column(Text, unique=False, nullable=False)
    img = Column(LargeBinary, unique=False, nullable=True)
    amount = Column(Integer, nullable=False, default=0)
    updated_at = Column(DateTime, unique=False, nullable=False)
    created_at = Column(DateTime, unique=False, nullable=False)

    def __repr__(self):
        return '<Prize {}>'.format(self.name)