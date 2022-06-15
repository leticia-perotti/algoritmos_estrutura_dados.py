from funcoes import *

n = True
lista = []
while n:
    opcao = input("Deseja colocar um elemento? S/N ")

    if opcao == 'S' or opcao == 's':
        valor = input("Digite um nome ")
        lista.append(valor)
    elif opcao =='N' or opcao == 'n':
        n = False
    else:
        print("Opção inválida")

lista = selectionSortLen(lista)
print(lista)