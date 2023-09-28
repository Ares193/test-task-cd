import sqlalchemy as sa

from sqlalchemy import Column, String, Integer, DateTime, func
from sqlalchemy.dialects.postgresql import UUID

from app.services.database.base import Base


class MetricDBModel(Base):
    __tablename__ = "metrics"

    id = Column(UUID, primary_key=True, index=True, nullable=False, server_default=sa.text("gen_random_uuid()"))
    service_name = Column(String, nullable=True)
    path = Column(String, nullable=True)
    response_time_ms = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())