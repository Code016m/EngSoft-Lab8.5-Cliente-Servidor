import json
from pathlib import Path

class InformacoesRepository:
    def __init__(self):
        self.arquivo = (
            Path(__file__).resolve().parents[2]
            / "data"
            / "livros.txt"
        )

    def consultar_informacoes(self):
        with open(self.arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        return {
            "horario": dados.get("horario", "Não informado."),
            "localizacao": dados.get("localizacao", "Não informada.")
        }
