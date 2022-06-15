from funcoes import *

n = True
listaNotas = []
listaMatriculas = []

while n:
    opcao = input("Deseja colocar um elemento? S/N")

    if opcao == 'S' or opcao == 's':
        matricula = int(input("Digite o numero de matricula "))
        listaMatriculas.append(matricula)

        notas = int(input("Digite a nota"))
        listaNotas.append(notas)

    elif opcao =='N' or opcao == 'n':
        n = False
    else:
        print("Opção inválida")

print("Ordenação por nota final")
notaFinal = bubbleSortListas(listaNotas, listaMatriculas)
print(notaFinal)

print("Ordenação por número de matriculas")
numeroMatricula = bubbleSortListas(listaMatriculas, listaNotas)
print(numeroMatricula)
