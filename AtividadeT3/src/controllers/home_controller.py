from models.home import Home

class HomeController: 
    def __init__(self) -> None:
        self._lista_de_produtos = []

    def produtos(self, titulo, preco, status):
        produto = Home(titulo, preco, status)
        self._lista_de_produtos.append(produto)
