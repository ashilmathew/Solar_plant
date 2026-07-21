from sqlalchemy import Column, Integer, String, Text, Enum, TIMESTAMP
from sqlalchemy.sql import func

from app.database.database import Base


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    address = Column(Text)

    email = Column(String(100))

    phone = Column(String(20))

    logo = Column(String(255))

    status = Column(
        Enum("ACTIVE", "INACTIVE"),
        default="ACTIVE"
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )