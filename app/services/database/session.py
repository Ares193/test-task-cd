from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.common.config import settings

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI), pool_size=10, pool_recycle=600, pool_pre_ping=True)
SessionLocal = sessionmaker(autoflush=False, bind=engine)


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_service = next(get_db())
