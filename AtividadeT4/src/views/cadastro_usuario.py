import streamlit as st
from src.controllers.usuario_controller import UsuarioController

class CadastroUsuario():

    def __init__(self) -> None:
        st.text("")
        st.text("")

        st.title("Cadastro")

        st.markdown("***")

        nome = st.text_input(
            label="Name",
                key = 1,
        )

        email = st.text_input(
            label="Email",
                key = 2,
        )

        senha = st.text_input(
            label="Senha",
                type = "password",
                    key = 3,
        )

        cpf = st.text_input(
            label="CPF",
                key = 4,
        )

        col1, col2 = st.columns(2)
        with col1:
            st.text("")
            st.button(label= "Voltar", on_click= UsuarioController.login_screen)
        with col2:
            st.text("")
            st.button(label= "Cadastrar", on_click= UsuarioController.sign_up, args = (UsuarioController(),nome, email, senha, cpf))