from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings
import os


def get_database_url(db_name: str) -> URL:
    # URL.create escapes special characters in the password (e.g. "@", "%")
    return URL.create(
        drivername="postgresql+psycopg2",
        username=settings.database_username,
        password=settings.database_password,
        host=settings.database_hostname,
        port=int(settings.database_port),
        database=db_name,
    )


if os.getenv("GITHUB_ACTIONS") == "true":
    db_name = settings.database_name + "_test"
else:
    db_name = settings.database_name

SQLALCHEMY_DATABASE_URL = get_database_url(db_name)

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
