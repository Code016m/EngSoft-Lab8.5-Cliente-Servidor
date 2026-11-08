from flask import Blueprint, jsonify
from modules.recomendacoes.service import RecomendacoesService

recomendacoes_bp = Blueprint("recomendacoes", __name__, url_prefix="/api")

service = RecomendacoesService()

@recomendacoes_bp.route("/recomendacoes", methods=["GET"])
def recomendar_livros():
    recomendacoes = service.recomendar_livros()
    return jsonify(recomendacoes), 200
