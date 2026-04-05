from sqlalchemy import Column, Integer, String # type of columns and base class
from sqlalchemy.orm import relationship # describe relationships between tables
from backend.core.database import Base # importing the base class for our models


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=True)

    pets = relationship("Report", back_populates="user",cascade="all, delete-orphan") #