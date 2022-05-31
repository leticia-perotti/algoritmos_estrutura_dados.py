def insereFim(listaCodigo, listaNome):
    verificaTamanho(listaCodigo, listaNome)

    codigo = int(input('Digite o código do produto'))
    nome = input('Digite o nome do produto')

    listaCodigo.append(codigo)
    listaNome.append(nome)

    return listaCodigo, listaNome

def insereInicio(listaCodigo, listaNome):

    if verificaExite(listaCodigo, 'inicio'):
        return 0

    verificaTamanho(listaCodigo, listaNome)
    tamanhoCodigo = len(listaCodigo) +1
    tamanhoNome = len(listaNome) +1
    print (tamanhoNome)

    codigo = int(input('Digite o código do produto'))
    nome = input('Digite o nome do produto')
    
    auxCodigo = [0] * tamanhoCodigo
    auxNome = [0] * tamanhoNome
    print(auxNome)

    for i in range(0, len(listaCodigo)):
        auxCodigo[i+1] = listaCodigo[i]

    auxCodigo[0] = codigo

    for i in range(len(listaNome)):
        auxNome[i+1] = listaNome[i]

    auxNome[0] = nome

    listaCodigo = auxCodigo
    listaNome = auxNome
    print(listaNome)
    print(listaCodigo)

    return listaCodigo, listaNome

def insereLocal(listaCodigo, listaNome):

    verificaTamanho(listaCodigo, listaNome)

    auxCodigo = listaCodigo.copy()
    auxNome = listaNome.copy()

    auxCodigo.append(0)
    auxNome.append(0)

    codigo = int(input('Digite o código do produto'))
    nome = input('Digite o nome do produto')
    indice = int(input('Digite o indice que deseja inserir'))

    if indice > len(listaCodigo):
        return print("O indice é maior que a própria lista!!")

    for i in range(indice,len(listaCodigo)):
        auxCodigo[i+1] = listaCodigo[i]
    
    for i in range(indice,len(listaNome)):
        auxNome[i+1] = listaNome[i]

    listaCodigo = auxCodigo
    listaNome = auxNome

    listaCodigo[indice]=codigo
    listaNome[indice]=nome
    print(listaCodigo)

    return listaCodigo,listaNome

def verificaTamanho(listaCodigo, listaNome):
    tamanhoCod = len(listaCodigo)
    tamanhoNo = len(listaNome)

    if tamanhoCod != tamanhoNo:
        print("Algo está errado, as listas tem tamanhos diferentes !!!!")
        exit()

def verificaExite(listaCodigo, acao):
    if acao == 'e' and len(listaCodigo) == 0:
        print("Algo está errado, não pode excluir de uma lista que não existe!")
        return True
    if acao == 'inicio' and len(listaCodigo) ==0:
        print("Algo está errado, não dá para inserir no início se nem existe inicio!!!!")
        return True
    return False


def excluir(listaCodigo,listaNome):
    verificaTamanho(listaCodigo, listaNome)
        
    verificaExite(listaCodigo, 'e')
    codigo = int(input('Digite o código do produto que deseja excluir'))
    
    num = ""
    for i in range(len(listaCodigo)):
        if listaCodigo[i] == codigo:
            num = i
            break

    if num!="":
        for i in range(num,len(listaCodigo)-1):
            listaCodigo[i]= listaCodigo[i+1]
            listaNome[i] = listaNome[i+1]

        listaCodigo[len(listaCodigo)-1]=0
        listaNome[len(listaNome)-1]=0
        return listaCodigo, listaNome

    print('O  elemento {} não se encontra na lista'.format(codigo))
    return -1

def localiza(listaCodigo, listaNome):
    if verificaTamanho(listaCodigo, listaNome):
        return 0

    codigo = int(input('Digite o código do produto que deseja achar o nome'))

    for i in range(len(listaCodigo)):
        if listaCodigo[i] == codigo:
            return print("O nome do produto" + listaNome[i])

def printar(listaCodigo, listaNome):
    verificaTamanho(listaCodigo, listaNome)

    print('Código | Nome')
    print(listaCodigo)
    print(listaNome)

    for i in range(0, len(listaCodigo)):
        print(listaCodigo[i], listaNome[i])

b = bool
b = True

listaCodigo = []
listaNome = []

while b:
    print('\n Bem vindo ao cadastro de produtos')
    print('\n 1 - Adicionar valor ao inicio da lista ')
    print('\n 2 - Adicionar valor ao fim da lista ')
    print('\n 3 - Adicionar valor em um local definido da lista ')
    print('\n 4 - Excluir elemento da lista')
    print('\n 5 - Localizar elemento na lista')
    print('\n 6 - Visualizar lista')
    print('\n 7 - Sair do sistema')
    opcao = int(input('Escolha sua opção '))

    if opcao == 7:
        b = False
    elif opcao == 1:
        if not(verificaExite(listaCodigo, 'inicio')):
            verificaTamanho(listaCodigo, listaNome)
            tamanhoCodigo = len(listaCodigo) +1
            tamanhoNome = len(listaNome) +1
            print (tamanhoNome)

            codigo = int(input('Digite o código do produto'))
            nome = input('Digite o nome do produto')
            
            auxCodigo = [0] * tamanhoCodigo
            auxNome = [0] * tamanhoNome
            print(auxNome)

            for i in range(0, len(listaCodigo)):
                auxCodigo[i+1] = listaCodigo[i]

            auxCodigo[0] = codigo

            for i in range(len(listaNome)):
                auxNome[i+1] = listaNome[i]

            auxNome[0] = nome

            listaCodigo = auxCodigo
            listaNome = auxNome
            print(listaNome)
            print(listaCodigo)
    elif opcao == 2:
        verificaTamanho(listaCodigo, listaNome)
        codigo = int(input('Digite o código do produto'))
        nome = input('Digite o nome do produto')

        listaCodigo.append(codigo)
        listaNome.append(nome)

    elif opcao == 3:        
        verificaTamanho(listaCodigo, listaNome)

        auxCodigo = listaCodigo.copy()
        auxNome = listaNome.copy()

        auxCodigo.append(0)
        auxNome.append(0)

        codigo = int(input('Digite o código do produto'))
        nome = input('Digite o nome do produto')
        indice = int(input('Digite o indice que deseja inserir'))

        if indice > len(listaCodigo):
            print("O indice é maior que a própria lista!!")
        else:
            for i in range(indice,len(listaCodigo)):
                auxCodigo[i+1] = listaCodigo[i]
            
            for i in range(indice,len(listaNome)):
                auxNome[i+1] = listaNome[i]

            listaCodigo = auxCodigo
            listaNome = auxNome

            listaCodigo[indice]=codigo
            listaNome[indice]=nome
            print(listaCodigo)

    elif opcao == 4:
        verificaTamanho(listaCodigo, listaNome)        
        verificaExite(listaCodigo, 'e')
        codigo = int(input('Digite o código do produto que deseja excluir'))
        
        num = ""
        for i in range(len(listaCodigo)):
            if listaCodigo[i] == codigo:
                num = i
                break

        if num!="":
            for i in range(num,len(listaCodigo)-1):
                listaCodigo[i]= listaCodigo[i+1]
                listaNome[i] = listaNome[i+1]

            listaCodigo[len(listaCodigo)-1]=0
            listaNome[len(listaNome)-1]=0
        else:
            print('O  elemento {} não se encontra na lista'.format(codigo))
        

    elif opcao == 5:
        if not(verificaTamanho(listaCodigo, listaNome)):
            codigo = int(input('Digite o código do produto que deseja achar o nome'))

            for i in range(len(listaCodigo)):
                if listaCodigo[i] == codigo:
                    print("O nome do produto" + listaNome[i])


    elif opcao == 6:
        verificaTamanho(listaCodigo, listaNome)

        print('Código | Nome')
        #print(listaCodigo)
        #print(listaNome)

        for i in range(0, len(listaCodigo)):
            print(listaCodigo[i], listaNome[i])

# As funções acima estão funcionando, mas passei elas para dentro do while pois suspeito de seu funcionamento
# depois de vários teste vi que o len do inserir no inicio retorna errado quando chamo a função
# por isso ta tudo dentro do while