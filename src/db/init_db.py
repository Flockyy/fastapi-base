from sqlalchemy.orm import Session

from core.config import settings
from base_class import Base # noqa: F401
from sqlalchemy import create_engine

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    
    engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)