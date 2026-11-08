from modules.favoritos.repository import FavoritosRepository

class FavoritosService:
    def __init__(self):
        self.repository = FavoritosRepository()

    def listar_favoritos(self):
        return self.repository.listar_favoritos()

    def adicionar_favorito(self, titulo):
        return self.repository.adicionar_favorito(titulo)

    def remover_favorito(self, titulo):
        return self.repository.remover_favorito(titulo)
