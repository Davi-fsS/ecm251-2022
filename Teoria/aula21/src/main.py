from views.lista_de_tarefas_view import ListaTarefasView
from controllers.tarefa_controller import TarefaController

# vai rodar ele primeiro
if __name__ == "__main__":
    tarefas_controller = TarefaController
    tarefas_view = ListaTarefasView(tarefas_controller)