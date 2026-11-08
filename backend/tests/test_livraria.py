import unittest
from app import create_app

class TestLivraria(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    # Testes de catálogo
    def test_listar_livros(self):
        response = self.client.get("/api/livros")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 7)

    def test_pesquisar_livros_por_titulo(self):
        response = self.client.get("/api/livros?q=Dom%20Casmurro")
        self.assertEqual(response.status_code, 200)
        livros = response.get_json()
        self.assertEqual(len(livros), 1)
        self.assertEqual(livros[0]["titulo"], "Dom Casmurro")

    def test_pesquisar_livros_por_autor(self):
        response = self.client.get("/api/livros?q=Machado%20de%20Assis")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 2)

    def test_consultar_livro_existente(self):
        response = self.client.get("/api/livros/Dom%20Casmurro")
        self.assertEqual(response.status_code, 200)
        livro = response.get_json()
        self.assertEqual(livro["titulo"], "Dom Casmurro")
        self.assertEqual(livro["autor"], "Machado de Assis")
        self.assertEqual(livro["preco"], 30.0)

    def test_consultar_livro_inexistente(self):
        response = self.client.get("/api/livros/Livro%20Inexistente")
        self.assertEqual(response.status_code, 404)

    def test_consultar_disponibilidade(self):
        response = self.client.get("/api/livros/Dom%20Casmurro/disponibilidade")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.get_json()["disponivel"])

    def test_consultar_disponibilidade_livro_indisponivel(self):
        response = self.client.get("/api/livros/Vidas%20Secas/disponibilidade")
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.get_json()["disponivel"])

    def test_consultar_disponibilidade_livro_inexistente(self):
        response = self.client.get("/api/livros/Livro%20Inexistente/disponibilidade")
        self.assertEqual(response.status_code, 404)

    # Testes de informações
    def test_consultar_informacoes(self):
        response = self.client.get("/api/informacoes")
        self.assertEqual(response.status_code, 200)
        informacoes = response.get_json()
        self.assertIn("horario", informacoes)
        self.assertIn("localizacao", informacoes)

    # Testes de recomendações
    def test_obter_recomendacoes(self):
        response = self.client.get("/api/recomendacoes")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.get_json()) > 0)

    # Testes de favoritos
    def test_listar_favoritos(self):
        response = self.client.get("/api/favoritos")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

    def test_adicionar_favorito(self):
        response = self.client.post("/api/favoritos", json={"titulo": "Dom Casmurro"})
        self.assertEqual(response.status_code, 200)
        favoritos = self.client.get("/api/favoritos").get_json()
        self.assertIn("Dom Casmurro", favoritos)

    def test_nao_adicionar_favorito_duplicado(self):
        self.client.post("/api/favoritos", json={"titulo": "Dom Casmurro"})
        self.client.post("/api/favoritos", json={"titulo": "Dom Casmurro"})
        favoritos = self.client.get("/api/favoritos").get_json()
        self.assertEqual(favoritos.count("Dom Casmurro"), 1)

    def test_adicionar_favorito_sem_titulo(self):
        response = self.client.post("/api/favoritos", json={})
        self.assertEqual(response.status_code, 400)

    def test_remover_favorito(self):
        self.client.post("/api/favoritos", json={"titulo": "Dom Casmurro"})
        response = self.client.delete("/api/favoritos/Dom%20Casmurro")
        self.assertEqual(response.status_code, 200)
        favoritos = self.client.get("/api/favoritos").get_json()
        self.assertNotIn("Dom Casmurro", favoritos)

if __name__ == "__main__":
    unittest.main(verbosity=2)
