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
        for item in self._item:
            self._item.remove(item)
        
    def exibir_itens(self):
        i = 0
        while(i < len(self._item)):
            print(self._item[i])
            i+=1
            
            
        