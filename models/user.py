from sqlalchemy import Column, Integer, String
from config.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    token = Column(String)
    adm = Column(String) # pode mexer em tudo
    tutor = Column(String) # pode adicionar/remover só os próprios animais
    veterinario = Column(String) # pode adicionar/remover qualquer animal