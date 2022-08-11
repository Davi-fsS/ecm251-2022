from item import Item
from carrinho import Carrinho

item1 = Item('Carregador', 'carrega iphone e android', 200.0)

item2 = Item(valor=350.0, nome='Stray', descricao='gato')

item3 = Item(valor=350.0, nome='Stray', descricao='gato')

print()
print(item1 == item2)
print(item2 == item3)
print(item1 == item3,'\n')

carrinho = Carrinho()

print(f'Tamanho: {carrinho.get_qtd_itens()}\nValor: {carrinho.get_valor_total()}\n')

carrinho.adicionar(item1)
carrinho.adicionar(item2)

print(f'Tamanho: {carrinho.get_qtd_itens()}\nValor: {carrinho.get_valor_total()}')

carrinho.remover(item1)

print(f'\nTamanho: {carrinho.get_qtd_itens()}\nValor: {carrinho.get_valor_total()}')

# Construção do menu
print("BEM VINDO!\nEscolha a operação a ser realizada:\n1-Adicionar itens\n2-Remover itens\n3- Quantidade de itens no carrinho\n4- Valor total do carrinho\n5- Sair")
