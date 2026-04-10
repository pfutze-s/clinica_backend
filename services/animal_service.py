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

    @staticmethod
    def get_animal(animal_id):
        session = SessionLocal()
        animal = session.query(Animal).filter(Animal.id == animal_id).first()
        session.close()
        return animal

    @staticmethod
    def delete_animal(animal_id):
        session = SessionLocal()
        animal = session.query(Animal).filter(Animal.id == animal_id).first()
        if not animal:
            
            session.close()
            return False
        
        session.delete(animal)
        session.commit()
        session.close()
        return True