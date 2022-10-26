from src.dao.pedido_dao import PedidoDAO
from src.controllers.item_controller import ItemController

class PedidoController:
    def __init__(self) -> None:
        pass
    
    def total_pedido(self, numero_pedido) -> float:
        items_pedido = PedidoDAO.get_instance().get_itens(numero_pedido)
        total = 0
        for(item_id, quantidade) in items_pedido:
            item = ItemController.pegar_item(item_id)
            total += item.preco * quantidade
        return total