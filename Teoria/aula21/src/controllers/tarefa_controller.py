# CONTROLLER - responsavel pelas funcionalidades

from models.tarefa import Tarefa            # importando a classe Tarefa do models

class TarefaController:
    def __init__(self) -> None:
        self._lista_de_tarefas = []        # armazenamento das tarefas
    
    def criar_nova_tarefa(self, descricao):
        tarefa = Tarefa(descricao)                 # tarefa vai receber a classe Tarefa com uma descricao
        self._lista_de_tarefas.append(tarefa)      # adicionando essa variavel para a lista

    def exibir_total_de_tarefas(self):
        return len(self._lista_de_tarefas)
    
    def exibir_tarefas_concluidas(self):
        total = 0
        if self.exibir_total_de_tarefas() != 0:
            for tarefa in self._lista_de_tarefas:
                if tarefa.get_concluida():
                    total += 1
            return total
        else:
            return 'nada'

    def get_tarefas(self):
        tarefas = []
        for tarefa in self._lista_de_tarefas:
            tarefas.append(
                {
                    'descricao':tarefa.get_descricao(),
                    'status':tarefa.get_concluida()
                }
            )
        return tarefas

    def mudar_status(self, indice):
        self._lista_de_tarefas[indice].set_concluida(
            not self._lista_de_tarefas[indice].get_concluida()    # inverte o status atual
        )