from sqlalchemy import Column, Integer, String, DateTime
from config.database import Base

class Consulta(Base):
    __tablename__ = "consultas"

    id = Column(Integer, primary_key=True)
    data_hora = Column(DateTime, nullable=False)
    status = Column(String, nullable=False, default="agendada")
    animal_id = Column(Integer, nullable=False)
    veterinario_id = Column(Integer, nullable=False)
    tutor_id = Column(Integer, nullable=False)