import streamlit as st
from models.carrinho import Carrinho

class CarrinhoController:
    def __init__(self):
        self._produtos = []
        self._precos = []
        self._total = 0

    def adicionando_no_carrinho(self, nome, preco):
        item = Carrinho(nome, preco)
        self._produtos.append(item)

    def get_total(self, preco):    #melhorar
        self._total += preco
        return self._total

    def pegar_total(self):
        resultado = 0.0
        for i in st.session_state.filme:
            resultado = resultado + i
        return resultado

    def get_tamanho_carrinho(self):
        return len(self._produtos)

    def get_produtos(self):              #melhorar
        produtos = []
        for carrinho in self._produtos:
            produtos.append(
                {
                    'titulo':carrinho[0],
                    'preco':carrinho[1]
                }
            )
        return produtos
