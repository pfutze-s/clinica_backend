from flask import Blueprint, request
from services.consulta_service import ConsultaService
from auth.decorators import role_required

consulta_bp = Blueprint("consulta_bp", __name__)

@consulta_bp.route("/consultas", methods=["POST"])
@role_required("adm")
def criar():
    data = request.json
    consulta = ConsultaService.create_consulta(data)
    return {"id": consulta.id, "status": consulta.status}, 201

@consulta_bp.route("/consultas", methods=["GET"])
@role_required("adm", "veterinario")
def listar():
    consultas = ConsultaService.list_consultas()
    return [
        {
            "id": c.id,
            "data_hora": str(c.data_hora),
            "status": c.status,
            "animal_id": c.animal_id,
            "veterinario_id": c.veterinario_id,
            "tutor_id": c.tutor_id
        }
        for c in consultas
    ]

@consulta_bp.route("/consultas/<int:consulta_id>", methods=["PATCH"])
@role_required("adm", "veterinario")
def atualizar_status(consulta_id):
    data = request.json
    consulta = ConsultaService.update_status(consulta_id, data["status"])
    if not consulta:
        return {"erro": "Consulta não encontrada"}, 404
    return {"id": consulta.id, "status": consulta.status}

@consulta_bp.route("/consultas/<int:consulta_id>", methods=["DELETE"])
@role_required("adm")
def deletar(consulta_id):
    ok = ConsultaService.delete_consulta(consulta_id)
    if not ok:
        return {"erro": "Consulta não encontrada"}, 404
    return {"mensagem": "Consulta removida com sucesso!"}