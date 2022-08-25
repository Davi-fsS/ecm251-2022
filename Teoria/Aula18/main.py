#Código para escrever dados em um arquivo

import os
from traceback import print_stack

try:
    arquivo = open("data/sistemas.txt","a")     #Cria arquivo novo, importante: "a" é de append

    continuar = True

    while continuar:
        os_name = input("Diga um OS: ")

        if(not os_name):                      #Verificar se a string ta vazia ou não 
            continuar = False
            continue

        arquivo.write(f'{os_name}\n')

    arquivo.close()

except FileNotFoundError:
    print("Caminho não existe, favor verificar.")

except Exception:
    print("Algo não esperado ocorreu: ")
    print_stack()
    
finally:
    print("Chegamos no final pessoal!")