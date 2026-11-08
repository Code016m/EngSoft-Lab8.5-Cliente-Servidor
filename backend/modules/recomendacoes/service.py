from modules.recomendacoes.repository import RecomendacoesRepository

class RecomendacoesService:
    def __init__(self):
        self.repository = RecomendacoesRepository()

    def recomendar_livros(self):
        livros = self.repository.listar_livros()
        favoritos = self.repository.listar_favoritos()
        recomendacoes = [
            livro for livro in livros
            if livro["titulo"] not in favoritos
        ]
        return recomendacoes
