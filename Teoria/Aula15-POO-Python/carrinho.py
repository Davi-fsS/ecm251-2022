#from item import Item

class Carrinho():
    #Método construtor
    def __init__(self):
        self._item = []

    #Métodos da classse
    def get_valor_total(self):
        total = 0
        for item in self._item:
            total += item.get_valor()
        return total

    def get_qtd_itens(self):
        return len(self._item)

    def adicionar(self,item):
        self._item.append(item)

    def remover(self,item):
        if item in self._item:
            self._item.remove(item)
            
        