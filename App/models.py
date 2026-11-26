from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import UUID, Text, Boolean, Column, text

class Base(DeclarativeBase):
    pass

class Monitor(Base):
    __tablename__ = 'monitors'
    uuid = Column(UUID, primary_key=True, server_default = text('gen_random_uuid()'))
    host = Column(Text, nullable=False)
    enabled = Column(Boolean, nullable=False)
