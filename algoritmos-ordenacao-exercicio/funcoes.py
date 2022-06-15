def selectionSortLen(lista):
    for i in range(len(lista)):
        min_idx = i
        for j in range(i+1, len(lista)):
            if len(lista[min_idx]) > len(lista[j]):
                min_idx = j    
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def bubbleSortListas(listaPrincipal, listaSegunda):
    tamanho = len(listaPrincipal)

    for i in range(tamanho):
        for j in range(tamanho-i-1):
            if listaPrincipal[j] > listaPrincipal[j+1]:
                temp = listaPrincipal[j]
                temp2 = listaSegunda[j]
                listaPrincipal[j] = listaPrincipal[j + 1]
                listaSegunda[j] = listaSegunda[j + 1]
                listaPrincipal[j+1] = temp
                listaSegunda[j+1] = temp2
    return listaPrincipal, listaSegunda

def pesquisaBinaria(lista, lista2,valor):
    lista1 = bubbleSortListas(lista, lista2)
    listaCerta = lista1[0]
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if listaCerta[meio] == valor:
            return meio
        elif listaCerta[meio] > valor:
            direita = meio - 1
        else:
            esquerda = meio + 1
    return -1


def pesquisaLinear(lista,valor):

    for i in range(len(lista)):
        if lista[i]==valor:
            return i

    return -1

