from sqlalchemy import Column, Integer, String
from config.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    token = Column(String)
    role = Column(String, nullable=False, default="adm")
    tutor_id = Column(Integer, nullable=True)