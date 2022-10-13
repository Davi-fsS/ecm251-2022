class Home:
    def __init__(self, titulo, preco, status) -> None:
        self._titulo = titulo
        self._preco = preco
        self._status = status

    def get_titulo(self):
        return self._titulo

    def get_preco(self):
        return self._preco

    def get_status(self):
        return self._status
    
    def __str__(self) -> str:
        return f"Home[Titulo: {self._titulo} - Preço: {self._preco} - Status adicionado: {self._status}]"