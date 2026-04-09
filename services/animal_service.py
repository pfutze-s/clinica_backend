from config.database import SessionLocal
from models.animal import Animal 

class AnimalService:

    @staticmethod
    def create_animal(data):
        session = SessionLocal()
        animal = Animal(**data)
        session.add(animal)
        session.commit()
        session.refresh(animal)
        session.close()
        return animal
    
    @staticmethod
    def list_animals():
        session = SessionLocal()
        animais = session.query(Animal).all()
        session.close()
        return animais    