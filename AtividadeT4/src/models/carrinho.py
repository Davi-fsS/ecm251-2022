# Davi Fernandes Simões Soares (20.01099-0)

class Carrinho():

    def __init__(self):
        self._filmes=[]   #_products

    def get_filmes(self):    #get products
        return self._filmes
    
    def set_filmes(self, filmes):
        self._filmes = filmes
        
    def __str__(self):
        return self._filmes