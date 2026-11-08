from modules.informacoes.repository import InformacoesRepository

class InformacoesService:
    def __init__(self):
        self.repository = InformacoesRepository()

    def consultar_informacoes(self):
        return self.repository.consultar_informacoes()