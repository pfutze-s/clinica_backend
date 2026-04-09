from flask import Blueprint, request
from services.animal_service import AnimalService
from auth.decorators import auth_required

animal_bp = Blueprint("animal_bp", __name__)

@animal_bp.route("/animais", methods=["POST"])
@auth_required
def criar():
    data = request.json
    animal = AnimalService.create_animal(data)
    return {"id": animal.id, "nome": animal.nome}, 201

@animal_bp.route("/animais", methods=["GET"])
@auth_required
def listar():
    animais = AnimalService.list_animals()
    return [
        {"id": a.id, "nome": a.nome, "especie": a.especie, "id_tutor": a.tutor_id}
        for a in animais
    ]