import json
from pathlib import Path

class CatalogoRepository:
    def __init__(self):
        self.arquivo = (
            Path(__file__).resolve().parents[2]
            / "data"
            / "livros.txt"
        )

    def listar_todos(self):
        with open(self.arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        return dados.get("livros", [])

    def buscar_por_titulo(self, titulo):
        livros = self.listar_todos()
        for livro in livros:
            if livro["titulo"].casefold() == titulo.casefold():
                return livro
        return None
