from re import I


class Item():
    def __init__(self, nome, descricao, valor):
        self._nome = nome
        self._descricao = descricao
        self._valor = valor

    def get_nome(self):
        return self._nome

    def get_descricao(self):
        return self._descricao

    def get_valor(self):
        return self._valor

    def __str__(self) -> str:
        return self._nome
    
    def __eq__(self, __o: object) -> bool:
        if(isinstance(__o, Item)):
            return self._nome == __o.get_nome()
        return False