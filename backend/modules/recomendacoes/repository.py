import json
from pathlib import Path

class RecomendacoesRepository:
    def __init__(self):
        self.arquivo = (
            Path(__file__).resolve().parents[2]
            / "data"
            / "livros.txt"
        )

    def listar_livros(self):
        with open(self.arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        return dados.get("livros", [])

    def listar_favoritos(self):
        with open(self.arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        return dados.get("favoritos", [])
