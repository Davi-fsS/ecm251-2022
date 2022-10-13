import streamlit as st
from controllers.carrinho_controller import CarrinhoController

class CarrinhoView:
    def __init__(self) -> None:
        
        self._carrinho = CarrinhoController()
        st.title('Carrinho')
        #st.subheader("Produtos adicionados: ")
        #st.text(f"1. {self._carrinho._produtos.get_titulo()}")
        #st.text(f"Preço: {self._carrinho._produtos.get_preco()}")

        st.subheader(f"Total no carrinho: R$ {self._carrinho.pegar_total()}")
        
        
        