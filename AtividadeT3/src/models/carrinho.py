from ast import iter_child_nodes
from mailbox import NotEmptyError


class Carrinho:
    def __init__(self,titulo, preco) -> None:
        self._titulo = titulo
        self._preco = preco
    
    def get_titulo(self):
        return self._titulo
    
    def get_preco(self):
        return self._preco
    
    def __str__(self) -> str:
        return f'Carrinho[Titulo: {self._titulo} - Preço: {self._preco}]'

    def __repr__(self) -> str:
        return f'Carrinho[Titulo: {self._titulo} - Preço: {self._preco}]'