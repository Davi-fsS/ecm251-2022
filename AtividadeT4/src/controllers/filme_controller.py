# Davi Fernandes Simões Soares (20.01099-0)

import streamlit as st
import time
from models.filme import Filme
from dao.dao_filme import FilmeDAO

class FilmeController:
    def __init__(self):
        self._filmes = FilmeDAO.get_instance().get_all()

    def get_filme(self,index):
        return self._filmes[index]
    
    def get_filmes(self):
        return self._filmes

    def sign_filme(self, nome, preco, url, saldo):
        filme = Filme(nome, preco, url, saldo)
        
        teste = FilmeDAO.get_instance().insert_filme(filme)
        if teste == False:
            st.session_state["carrinho"] = "Falha ao Cadastrar"
        else:
            st.session_state["carrinho"] = "Produto Cadastrado Com Sucesso"
            st.session_state["Login"] = "negado"
            time.sleep(0.2)
            st.session_state["Login"] = "aprovado"