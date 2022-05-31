
def tamanhoFila(fila):
    if not fila:
        return print('É necessario criar a Fila')
    return print('Tamanho da Fila: ',quantidade)


def filaCheia(fila):
    if not fila:
        return print('É necessario criar a fila')
    if quantidade==max:
        return True

def inserirFila(fila,valor):
    global quantidade,fim
    if not fila:
        return print('É necessario criar a pilha')
    if filaCheia(fila):
        return print('Pilha cheia')
    fila[fim]=valor
    fim= (fim+1)%max
    quantidade+=1

def removeFila(fila):
     global quantidade,inicio
     if not fila or quantidade==0:
        return print('É necessario criar a pilha')
     inicio= (inicio+1)%max
     quantidade-=1

def consultaFila(fila):
    if not fila or quantidade==0:
        return print('É necessario criar a pilha')
    return print(fila[inicio])

def mostrarFila(fila):
    if quantidade == 0:
        print('Fila vazia')
    else:
        print('\n'*5)
        for i in range(inicio,quantidade):
            print(fila[i])
        for i in range(fim):
            print(fila[i])

max = 10
quantidade = 0
inicio=0
fim=0

b = bool
b = True
filaPessoa = ['']
filaPrioridade = ['']
aux = 0

while b:
    print('\nBem Vindo ao Banco!')
    print('\n1 - Inserir na fila')
    print('\n2 - Chamar próximo')
    print('\n3 - Ver a fila')
    print('\n4 - Sair')

    opcao = int(input("Digite sua opção"))

    if opcao == 4:
        b = False
    elif opcao == 1:
        if filaCheia(filaPessoa):
            print('Pilha cheia')
        else:
            nome = input("Digite o nome da pessoa")
            prioridade = int(input("1 - com preferencia \n2-Sem prefereicia"))

            filaPessoa.append(nome)
            filaPrioridade.append(prioridade)
    elif opcao == 2:
        if len(filaPessoa) == 0:
            print('É necessario criar a fila')
        else:
            if not(1 in filaPrioridade):
                for i in range(0,len(filaPessoa)):
                    if filaPrioridade[i] != 0 and filaPrioridade[i]!= '':
                        print('3')
                        print(filaPrioridade[i])
                        print('Chamando pessoa'+filaPessoa[i])
                        filaPrioridade[i]=0
                        filaPessoa[i]=0
                        break
            else:
                for i in range(0,len(filaPessoa)):
                    if filaPrioridade[i]== 1 and aux != 2:
                        print('1')
                        print('Chamando pessoa'+filaPessoa[i])
                        filaPrioridade[i]=0
                        filaPessoa[i]=0
                        aux = aux + 1
                        break
                    elif filaPrioridade[i]== 2 and aux == 2:
                        print('2')
                        print('Chamando pessoa'+filaPessoa[i])
                        filaPrioridade[i]=0
                        filaPessoa[i]=0
                        aux = 0
                        break


    elif opcao == 3:
        print('Pessoa | Prioridade')
        for i in range(len(filaPessoa)):
            print(filaPessoa[i], filaPrioridade[i])
            








