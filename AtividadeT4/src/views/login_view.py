import streamlit as st
from src.controllers.usuario_controller import UsuarioController

class LoginView():

    def __init__(self):
        st.text("")
        st.text("")

        st.title("Login")

        st.markdown("***")

        email = st.text_input(
            label="Email",
            value = "abc@gmail.com"
        )

        senha = st.text_input(
            label="Senha",
            type = "password",
            value= "123"
        )
        
        st.text("")
        
        col1, col2 = st.columns(2)
        with col1:
            st.button(label= "Entrar", on_click= UsuarioController.check_login, args = (UsuarioController(),email,senha))
        with col2:
            st.button(label = "Novo registro", on_click = UsuarioController.sign_up_screen)