import streamlit as st
from src.controllers.filme_controller import FilmeController

class CadastroView():

    def __init__(self):

        st.text("")
        st.text("")
        st.title("Cadastro De Filmes")
        
        nome1 = st.text_input(
            label= "Nome",
                key = 190,
        )
        preco1 = st.number_input(
            label="Preço",
                key = 191,
        )
        url1 = st.text_input(
            label="URL da capa do filme",
                key = 192,
        )
        saldo1 = st.number_input(
            label = "Quantidade",
                key = 193,
        )
        
        st.text("")
        st.button(label= "Cadastrar produto", on_click= FilmeController.sign_filme, args = (FilmeController(), nome1, preco1, url1, saldo1))
        
        st.markdown("### " + st.session_state["carrinho"])
    