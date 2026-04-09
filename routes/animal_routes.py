from flask import Blueprint, request
from services.animal_service import AnimalService
from auth.decorators import auth_required, role_required

animal_bp = Blueprint("animal_bp", __name__)

@animal_bp.route("/animais", methods=["POST"])
@auth_required
@role_required("adm", "tutor", "veterinario")
def criar():
    data = request.json
    animal = AnimalService.create_animal(data)
    return {"id": animal.id, "nome": animal.nome}, 201

@animal_bp.route("/animais", methods=["GET"])
@auth_required
@role_required("adm")
def listar():
    animais = AnimalService.list_animals()
    return [
        {"id": a.id, "nome": a.nome, "especie": a.especie, "id_tutor": a.tutor_id}
        for a in animais
    ]

@animal_bp.route("/animais/<int:animal_id>", methods=["GET"])
@auth_required
@role_required("adm")
def obter(animal_id):
    animal = AnimalService.get_animal(animal_id)
    if not animal:
        return {"erro": "Animal não encontrado"}, 404
    return {"id": animal.id, "nome": animal.nome, "especie": animal.especie, "id_tutor": animal.tutor_id}


@animal_bp.route("/animal/<int:animal_id>", methods=["PUT"])
@auth_required
@role_required("adm")
def atualizar(animal_id):
    data = request.json
    animal = AnimalService.update_animal(animal_id, data)
    if not animal:
       return {"erro": "Animal não encontrado"}, 404
    return {"id": animal.id, "nome": animal.nome, "especie": animal.especie, "id_tutor": animal.tutor_id}

@animal_bp.route("/animais/<int:animal_id>", methods=["DELETE"])
@auth_required
@role_required("adm", "tutor", "veterinario")
def deletar(animal_id):
    ok = AnimalService.delete_animal(animal_id)
    if not ok:
        return {"erro": "Animal não encontrado"}, 404
    return {"mensagem": "Animal removido com sucesso!"}