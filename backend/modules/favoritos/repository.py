import json
from pathlib import Path

class FavoritosRepository:
    def __init__(self):
        self.arquivo = (
            Path(__file__).resolve().parents[2]
            / "data"
            / "livros.txt"
        )

    def listar_favoritos(self):
        with open(self.arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        return dados.get("favoritos", [])

    def adicionar_favorito(self, titulo):
        with open(self.arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        favoritos = dados.get("favoritos", [])
        if titulo not in favoritos:
            favoritos.append(titulo)
        dados["favoritos"] = favoritos
        with open(self.arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        return favoritos

    def remover_favorito(self, titulo):
        with open(self.arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        favoritos = dados.get("favoritos", [])
        if titulo in favoritos:
            favoritos.remove(titulo)
        dados["favoritos"] = favoritos
        with open(self.arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        return favoritos
