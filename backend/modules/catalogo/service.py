from modules.catalogo.repository import CatalogoRepository

class CatalogoService:
    def __init__(self):
        self.repository = CatalogoRepository()

    def listar_livros(self, pesquisa=None):
        livros = self.repository.listar_todos()
        if pesquisa:
            pesquisa = pesquisa.casefold()
            livros = [
                livro for livro in livros
                if pesquisa in livro["titulo"].casefold()
                or pesquisa in livro["autor"].casefold()
            ]
        return livros

    def consultar_livro(self, titulo):
        return self.repository.buscar_por_titulo(titulo)

    def consultar_disponibilidade(self, titulo):
        livro = self.repository.buscar_por_titulo(titulo)
        if livro is None:
            return None
        return {
            "titulo": livro["titulo"],
            "disponivel": livro["disponivel"]
        }
