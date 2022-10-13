from models.login import Login
import streamlit as st

class LoginController:
    def __init__(self) -> None:
        pass

    def logar(self, usuario, senha):
        if(usuario == "aaa" and senha == "123"):
            login = Login(usuario, senha, True)
        else:
            login = Login(usuario, senha, False)
        st.session_state['statusBotao'] = login.get_status_botao()
        
        
        
        

        
