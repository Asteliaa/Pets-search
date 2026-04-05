from sqlalchemy import create_engine #, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base #, scoped_session
from backend.core.config import get_db_url #, settings

DATABASE_URL = get_db_url() #settings.database_url

engine = create_engine(DATABASE_URL, echo=True) #, pool_pre_ping=True
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #, expire_on_commit=False
Base = declarative_base() #metadata = MetaData()