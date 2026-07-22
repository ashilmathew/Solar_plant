from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Date,
    Enum,
    ForeignKey,
    TIMESTAMP,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base


class Plant(Base):
    __tablename__ = "plants"

    id = Column(Integer, primary_key=True, index=True)

    organization_id = Column(
        Integer,
        ForeignKey("organizations.id", ondelete="CASCADE"),
        nullable=False,
    )

    plant_name = Column(String(100), nullable=False)

    capacity_kw = Column(Float, nullable=False)

    location = Column(String(255))

    latitude = Column(Float)

    longitude = Column(Float)

    commissioning_date = Column(Date)

    status = Column(
        Enum("ACTIVE", "INACTIVE"),
        default="ACTIVE",
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.now(),
    )

    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now(),
    )

    organization = relationship("Organization", back_populates="plants")