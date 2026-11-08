from flask import Flask, jsonify

from modules.catalogo import catalogo_bp
from modules.favoritos import favoritos_bp
from modules.informacoes import informacoes_bp
from modules.recomendacoes import recomendacoes_bp


def create_app():
    """Cria a aplicação responsável exclusivamente pela API REST."""
    app = Flask(__name__)

    # Permite que o front-end hospedado separadamente consuma a API.
    @app.after_request
    def adicionar_cors(response):
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, DELETE, OPTIONS"
        return response

    app.register_blueprint(catalogo_bp)
    app.register_blueprint(favoritos_bp)
    app.register_blueprint(informacoes_bp)
    app.register_blueprint(recomendacoes_bp)

    @app.route("/", methods=["GET"])
    def health_check():
        return jsonify({
            "mensagem": "API da Livraria funcionando!",
            "endpoints": [
                "/api/livros",
                "/api/favoritos",
                "/api/informacoes",
                "/api/recomendacoes"
            ]
        }), 200

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
