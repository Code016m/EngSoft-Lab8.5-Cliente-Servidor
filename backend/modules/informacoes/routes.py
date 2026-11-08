from flask import Blueprint, jsonify
from modules.informacoes.service import InformacoesService

informacoes_bp = Blueprint("informacoes", __name__, url_prefix="/api")

service = InformacoesService()

@informacoes_bp.route("/informacoes", methods=["GET"])
def consultar_informacoes():
    informacoes = service.consultar_informacoes()
    return jsonify(informacoes), 200