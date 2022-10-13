import streamlit as st
from views.login_view import LoginView, HomeView
from controllers.login_controller import LoginController

class IniciaLogin:
    def __init__(self):
        
        if st.session_state.statusBotao == False:
            st.session_state['telaAtual'] = LoginView(LoginController)
        if st.session_state.statusBotao == True:
            st.session_state['telaAtual'] = HomeView()

    