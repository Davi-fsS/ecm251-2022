from ast import iter_child_nodes
from tokenize import Double
from item import Item
from carrinho import Carrinho

# item1 = Item('Carregador', 'carrega iphone e android', 200.0)

# item2 = Item(valor=350.0, nome='Stray', descricao='gato')

# item3 = Item(valor=350.0, nome='Stray', descricao='gato')

# print()
# print(item1 == item2)
# print(item2 == item3)
# print(item1 == item3,'\n')

# carrinho = Carrinho()

# print(f'Tamanho: {carrinho.get_qtd_itens()}\nValor: {carrinho.get_valor_total()}\n')

# carrinho.adicionar(item1)
# carrinho.adicionar(item2)

# print(f'Tamanho: {carrinho.get_qtd_itens()}\nValor: {carrinho.get_valor_total()}')

# carrinho.remover(item1)

# print(f'\nTamanho: {carrinho.get_qtd_itens()}\nValor: {carrinho.get_valor_total()}')

carrinho = Carrinho()

# Construção do menu
print("BEM VINDO!")
op = 0
i = 0
while(op!=6):

    print("\n******* MENU *******\n1-Adicionar itens\n2-Remover itens\n3- Quantidade de itens no carrinho\n4- Valor total do carrinho\n5- Itens no carrinho\n6- Sair\n")
    op = int(input('Escolha a operação a ser realizada: '))

    
    if(op == 1):
        nome = input('Digite o nome do produto: ')
        descricao = input(f'Digite a descricao do produto {nome}: ')
        valor = float(input(f'Digite o valor do produto {nome}: '))
        carrinho.adicionar(Item(nome,descricao,valor))
        print(carrinho._item[i])
        i+=1

    if(op == 2):
        nomeRemover = input('Digite o nome do produto a ser removido: ')
        carrinho.remover(nomeRemover)
        
    if(op == 3):
        item = 'item'
        if(carrinho.get_qtd_itens() > 0):
            item = 'itens'
        print(f'A quantidade de itens no carrinho é de: {carrinho.get_qtd_itens()} {item}')
        
    if(op == 4):
        print(f'O valor total do carrinho é de: R$ {carrinho.get_valor_total()}')

    if(op == 5):
        carrinho.exibir_itens()

print('OBRIGADO!')