from sqlalchemy import Column, Integer, String
from config.database import Base

class Tutor(Base):
    __tablename__ = "tutores"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    telefone = Column(String)
    email = Column(String)