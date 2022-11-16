import streamlit as st
from src.controllers.usuario_controller import UsuarioController
from src.views.perfil_view import PerfilView

class SideBarHomeView():
    def __init__(self):

        st.text("")
        st.title(f"Loja de Filmes!")
        PerfilView()
        st.button(label= "Sair", on_click= UsuarioController.logout)