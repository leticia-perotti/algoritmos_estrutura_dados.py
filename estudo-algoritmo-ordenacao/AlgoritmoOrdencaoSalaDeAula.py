
#Selection Sort
def selectionSort(lista):
    listaOrdenada = []
    tam = len(lista)
    for i in range(tam):
        menor = lista[0]
        for j in range(len(lista)):
            if lista[j]<menor:
                menor = lista[j]
                pos_menor=j
        listaOrdenada.append(menor)
        lista.remove(menor)
    return listaOrdenada
#aleatorio, random, descrescente, 1 valor é o maior(sem o um)
