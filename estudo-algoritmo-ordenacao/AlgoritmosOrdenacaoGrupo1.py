############ Grupo 1 #############


def bubbleSort(lista):
    tamanho = len(lista)
    aux = lista[:]

    for i in range(tamanho):
        for j in range(tamanho-i-1):
            if aux[j] > aux[j+1]:
                temp = aux[j]
                aux[j] = aux[j + 1]
                aux[j+1] = temp
    return aux

def insertion_sort(lista):
    n = len(lista)
    for i in range(1,n):
        chave = lista[i]
        j = i - 1
        while j>= 0 and lista[j]>chave:
            lista[j+1]= lista[j]
            j = j - 1
        lista[j+1] = chave
    return lista


def particao(lista, inicio, fim):

    pivo = lista[fim - 1]
    for i in range(inicio, fim):
        if lista[i] > pivo:
            fim += 1
        else:
            fim += 1
            inicio += 1
            lista[i], lista[inicio - 1] = lista[inicio - 1], lista[i]
    return inicio- 1

def quick(lista, inicio=0, fim=None): #lista, inicio da lista, fim da lista
    fim = fim if fim is not None else len(lista)
    if inicio < fim:
        odio = particao(lista, inicio, fim)
        quick(lista, inicio, odio)
        quick(lista, odio + 1, fim)
    return lista


def shell_sort(lista):
    n = len(lista)
    h = n // 2
    while h > 0:
        for i in range(h, n):
            t = lista[i]
            j = i
            while j >= h and lista[j - h] > t:
                lista[j] = lista[j - h]
                j -= h

            lista[j] = t
        h = h // 2
    return lista
