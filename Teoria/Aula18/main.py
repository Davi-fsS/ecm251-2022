#Código para escrever dados em um arquivo

import os


arquivo = open("data/sistemas.txt","a")     #Cria arquivo novo, importante: "a" é de append

continuar = True

while continuar:
    os_name = input("Diga um OS: ")
    
    if(not os_name):                      #Verificar se a string ta vazia ou não 
        continuar = False
        continue

    arquivo.write(f'{os_name}\n')

arquivo.close()