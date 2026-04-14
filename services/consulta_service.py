from config.database import SessionLocal
from models.consulta import Consulta

class ConsultaService:

    @staticmethod
    def create_consulta(data):
        session = SessionLocal()
        consulta = Consulta(**data)
        session.add(consulta)
        session.commit()
        session.refresh(consulta)
        session.close()
        return consulta

    @staticmethod
    def list_consultas():
        session = SessionLocal()
        consultas = session.query(Consulta).all()
        session.close()
        return consultas

    @staticmethod
    def get_consulta(consulta_id):
        session = SessionLocal()
        consulta = session.query(Consulta).filter(Consulta.id == consulta_id).first()
        session.close()
        return consulta

    @staticmethod
    def update_status(consulta_id, status):
        session = SessionLocal()
        consulta = session.query(Consulta).filter(Consulta.id == consulta_id).first()
        if not consulta:
            session.close()
            return None
        consulta.status = status
        session.commit()
        session.refresh(consulta)
        session.close()
        return consulta

    @staticmethod
    def delete_consulta(consulta_id):
        session = SessionLocal()
        consulta = session.query(Consulta).filter(Consulta.id == consulta_id).first()
        if not consulta:
            session.close()
            return False
        session.delete(consulta)
        session.commit()
        session.close()
        return True