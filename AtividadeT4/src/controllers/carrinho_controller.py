# Davi Fernandes Simões Soares (20.01099-0)

import streamlit as st
from src.models.carrinho import Carrinho
from src.dao.dao_filme import FilmeDAO

class CarrinhoController():
    def __init__(self):
        self._carrinho = Carrinho()
        
    def get_carrinho(self):
        return self._carrinho

    def add_filme(self,filme,qtd):
        for i in range(len(self.get_carrinho().get_filmes())):
            if self.get_carrinho().get_filmes()[i][0].get_nome() == filme.get_nome() and qtd <= filme.get_saldo():
                if self.get_carrinho().get_filmes()[i][1] + qtd <= filme.get_saldo():
                    self.get_carrinho().get_filmes()[i][1] += qtd
                    st.session_state["falta"] = ""
                    
                else:
                    st.session_state["falta"] = f"{filme.get_nome()} tem somente {filme.get_saldo()} unidade(s) disponível(is) em estoque"
                return
        self.get_carrinho().get_filmes().append([filme,qtd])

    def get_total_preco(self):
        total = 0
        for items in self.get_carrinho().get_filmes():
            total += items[0].get_preco() * items[1]
        return total
    
    def limpar_carrinho(self):
        try:
            for item in self.get_carrinho().get_filmes():
                if item[0].get_saldo() - item[1] >= 0:
                    item[0].set_saldo(item[0].get_saldo() - item[1])
                FilmeDAO.get_instance().update_filme(item[0])
            self.get_carrinho().set_filmes([])
            return True
        except:
            return False

