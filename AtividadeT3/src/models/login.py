import streamlit as st
class Login:

    def __init__(self,usuario, senha, status_botao = False):
        self._usuario = usuario
        self._senha = senha
        self._status_botao = status_botao

    def get_usuario(self):
        return self._usuario

    def get_senha(self):
        return self._senha
    
    def get_status_botao(self):
        return self._status_botao

    def __str__(self) -> str:
        return f'Login[Usuario: {self._usuario} - Senha: {self._senha} - Status: {self._status_botao}]'