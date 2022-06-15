
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


nome=input("digite um nome:")
print(bubbleSort(list(nome)))

