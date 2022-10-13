from faulthandler import disable
import streamlit as st
from views.home_view import HomeView
from controllers.login_controller import LoginController

class LoginView:
    def __init__(self, controller) -> None:
        self.usuario = st.text_input(label="Usuário", placeholder="Usuario é: aaa" ,value="",type="default",key="usuario1")
        self.senha = st.text_input(label="Senha", placeholder="Digite sua senha...", value="123",type="password",key="password1")
        self.controller = LoginController()
        st.button(label="Entrar",help="Clique aqui",on_click=self.controller.logar(self.usuario, self.senha), key="pressed")
        if st.session_state.pressed == "True":
            st.session_state.pressed = True
    
    def get_button(self):
        return self._button
    
    def show_menu(self):
        if st.session_state['statusBotao']:
            st.session_state['telaAtual'] = HomeView()
