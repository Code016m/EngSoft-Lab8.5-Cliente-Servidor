from flask import Blueprint, jsonify, request
from modules.catalogo.service import CatalogoService

catalogo_bp = Blueprint("catalogo", __name__, url_prefix="/api")

service = CatalogoService()

@catalogo_bp.route("/livros", methods=["GET"])
def listar_livros():
    pesquisa = request.args.get("q")
    livros = service.listar_livros(pesquisa)
    return jsonify(livros), 200

@catalogo_bp.route("/livros/<titulo>", methods=["GET"])
def consultar_livro(titulo):
    livro = service.consultar_livro(titulo)
    if livro is None:
        return jsonify({"erro": "Livro não encontrado."}), 404
    return jsonify(livro), 200

@catalogo_bp.route("/livros/<titulo>/disponibilidade", methods=["GET"])
def consultar_disponibilidade(titulo):
    disponibilidade = service.consultar_disponibilidade(titulo)
    if disponibilidade is None:
        return jsonify({"erro": "Livro não encontrado."}), 404
    return jsonify(disponibilidade), 200
