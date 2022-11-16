# Davi Fernandes Simões Soares (20.01099-0)

import streamlit as st
from src.models.usuario import Usuario
from src.controllers.carrinho_controller import CarrinhoController
from src.dao.dao_usuario import UsuarioDAO
import time

class UsuarioController():
    def __init__(self):
        self._usuarios = UsuarioDAO.get_instance().get_all()

    def check_login(self, email, senha):
        usuario_json = {}
        for user in self._usuarios:
            usuario_email = user.get_email()
            senha = user.get_senha()
            usuario_json[usuario_email] = (senha, [user.get_nome(), user.get_cpf()])

        try:
            if usuario_json[email][0] == senha:
                st.session_state["Login"] = "aprovado"
                st.session_state['Usuario'] = usuario_json[email][1][0] 
                st.session_state['Cpf'] = usuario_json[email][1][1]     
                st.session_state['Email'] = email                    
                
            else:
                st.session_state["Login"] = "errado"

        except KeyError:

            st.session_state["Login"] = "errado"
            

    def sign_up(self, nome, email, senha, cpf):
        usuario = Usuario(nome, email, senha, cpf)
       
        try:
            UsuarioDAO.get_instance().insert_user(usuario)
            st.markdown("### Registrado")
        except:
            st.markdown("### Email ou cpf já registrados")

    def logout():
        st.session_state["Login"] = "negado"
        st.session_state["Cart"] = CarrinhoController()
    
    def change_data(self, email, senha):
        usuario = Usuario(st.session_state['Usuario'], email, senha, st.session_state['Cpf'])
        try:
            UsuarioDAO.get_instance().update_user(usuario)
            st.markdown("### Alterações Sucesso")
        except:
            st.markdown("### Email já registrado")
    
    def change_login_data():
        st.session_state["Profile"] = "change"

    def go_back():
        st.session_state["Profile"] = "dados"
    
    def sign_up_screen():
        st.session_state["Login"] = "registro"
    
    def login_screen():
        st.session_state["Login"] = "negado"
    
    def home_screen():
        st.session_state["Login"] = "negado"
        time.sleep(0.2)
        st.session_state["Login"] = "aprovado"