from turtle import onclick
import streamlit as st
from controllers.tarefa_controller import TarefaController

class ListaTarefasView:
    def __init__(self, controller) -> None:
       self.descricao_tarefa = st.text_input('Insira a sua tarefa aqui...')
       self.controller = TarefaController()
       self.bot_adicionar = st.button("Add tarefa", on_click=self.adicionar_tarefa)

    def adicionar_tarefa(self):
        self.controller.criar_nova_tarefa(self.descricao_tarefa)