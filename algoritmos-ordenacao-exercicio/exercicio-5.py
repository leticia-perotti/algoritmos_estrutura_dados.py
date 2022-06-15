from funcoes import *

n = True
listaNotas = []
listaMatriculas = []

while n:
    menuOpcao = int(input("Deseja: \n1-Adicionar Elemento\n2-Buscar Maticula \n3-Buscar Nota \n4-Sair"))

    if menuOpcao == 4:
        b = False
    elif menuOpcao == 3 or menuOpcao == 2:
        opcaoOrdenacao = int(input("Deseja odenar por \n1-Busca Binária \n2-Busca Linear"))

        if opcaoOrdenacao == 1:
            if menuOpcao == 3:
                nota = int(input("Digite a nota que deseja buscar"))
                index = pesquisaBinaria(listaNotas, listaMatriculas, nota)
                if index != -1:
                    print("A nota" + str(listaNotas[index]) + "é da matricula" + str(listaMatriculas[index]))
                else:
                    print("Erro")
            else:
                matricula = int(input("Digite a matricula que deseja buscar"))
                index = pesquisaBinaria(listaMatriculas, listaNotas, matricula)
                if index != -1:
                    print("A matricula" + str(listaMatriculas[index]) + "é da nota" + str(listaNotas[index]))
                else:
                    print("Erro")
        else:
            if menuOpcao == 3:
                nota = int(input("Digite a nota que deseja buscar"))
                index = pesquisaLinear(listaNotas, nota)
                if index != -1:
                    print("A nota" + str(listaNotas[index]) + "é da matricula" + str(listaMatriculas[index]))
                else:
                    print("Erro")
            else:
                matricula = int(input("Digite a matricula que deseja buscar"))
                index = pesquisaLinear(listaMatriculas, matricula)
                if index != -1:
                    print("A matricula" + str(listaMatriculas[index]) + "é da nota" + str(listaNotas[index]))
                else:
                    print("Erro")


    elif menuOpcao == 1:
        matricula = int(input("Digite o numero de matricula "))
        listaMatriculas.append(matricula)

        notas = int(input("Digite a nota"))
        listaNotas.append(notas)