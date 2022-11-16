import streamlit as st
from src.controllers.usuario_controller import UsuarioController

class PerfilView():

    def __init__(self):

        st.write("")
        st.markdown("***")
        st.title("Perfil")              

        if st.session_state["Profile"] == "dados":
            st.markdown(f"### Nome: {st.session_state['Usuario']}")
            st.markdown(f"##### Email: {st.session_state['Email']}")
            if(st.session_state['Cpf'] == ''):
                pass
            else:
                st.markdown(f"### CPF: {st.session_state['Cpf']}")
            st.button("Mudar informações de login", key = 7852084, on_click = UsuarioController.change_login_data)
        if st.session_state["Profile"] == "change":
            email = st.text_input(
                label="Novo Email",
                    key = 82700,
            )
            senha = st.text_input(
                label="Nova Senha",
                    type = "password",
                        key = 56240,
            )
            col3, col4 = st.columns(2)
            with col3:
                st.button(label = "Voltar", key = 99785, on_click = UsuarioController.go_back)
            
            with col4:
                st.button(label= "Alterar", key = 1234675, on_click= UsuarioController.change_data, args = (UsuarioController(), email, senha))
    
        st.markdown("***")
        st.write("")