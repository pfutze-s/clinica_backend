from config.database import SessionLocal
from models.tutor import Tutor 

class TutorService:

    @staticmethod
    def create_tutor(data):
        session = SessionLocal()
        tutor = Tutor(**data)
        session.add(tutor)
        session.commit()
        session.refresh(tutor)
        session.close()
        return tutor
    
    @staticmethod
    def list_tutores():
        session = SessionLocal()
        tutores = session.query(Tutor).all()
        session.close()
        return tutores    