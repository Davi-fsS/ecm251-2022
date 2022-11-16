# Davi Fernandes Simões Soares (20.01099-0)

class Filme():
    def __init__(self, nome, preco, url, saldo):
        self._nome = nome
        self._preco = preco
        self._url = url
        self._saldo = saldo

    def get_nome(self):
        return self._nome
        
    def get_preco(self):
        return self._preco

    def get_url(self):
        return self._url
    
    def get_saldo(self):
        return self._saldo
    
    def set_saldo(self, saldo):
        self._saldo = saldo

    def __str__(self):
        return f'Filme(nome:{self.get_nome()}, price:{self.get_preco()}, url:{self.get_url()}, amount:{self.get_saldo()})'