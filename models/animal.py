from sqlalchemy import Column, Integer, String
from config.database import Base

class Animal(Base):
    __tablename__ = "animais"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    especie = Column(String)
    tutor_id = Column(Integer)