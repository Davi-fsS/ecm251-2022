import streamlit as st
from iniciador import IniciaLogin

if __name__ == "__main__":

    st.session_state.statusBotao = False
    IniciaLogin()
    