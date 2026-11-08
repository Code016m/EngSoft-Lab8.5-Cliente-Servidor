from flask import Blueprint, jsonify, request
from modules.favoritos.service import FavoritosService

favoritos_bp = Blueprint("favoritos", __name__, url_prefix="/api")

service = FavoritosService()

@favoritos_bp.route("/favoritos", methods=["GET"])
def listar_favoritos():
    favoritos = service.listar_favoritos()
    return jsonify(favoritos), 200

@favoritos_bp.route("/favoritos", methods=["POST"])
def adicionar_favorito():
    dados = request.get_json()
    if not dados or not dados.get("titulo"):
        return jsonify({"erro": "Título não informado."}), 400
    favoritos = service.adicionar_favorito(dados["titulo"])
    return jsonify(favoritos), 200

@favoritos_bp.route("/favoritos/<titulo>", methods=["DELETE"])
def remover_favorito(titulo):
    favoritos = service.remover_favorito(titulo)
    return jsonify(favoritos), 200
