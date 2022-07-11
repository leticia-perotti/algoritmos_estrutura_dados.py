
############ Grupo 0 #############

#combSort!
def CombSort(lista):
    shrink = 1.3
    gaps = len(lista)
    swapped = True
    i = 0

    while gaps > 1 or swapped:
        gaps = int(float(gaps) / shrink)

        swapped = False
        i = 0

        while gaps + i < len(lista):
            if lista[i] > lista[i+gaps]:
                lista[i], lista[i+gaps] = lista[i+gaps], lista[i]
                swapped = True
            i += 1
    return lista

# HEAP SORT

from heapq import heappop, heappush

def heap_sort(lista):
    heap = []
    for i in lista:
        heappush(heap, i)

    ordenada = []

    # Enquanto temos elementos restantes no heap
    while heap:
        ordenada.append(heappop(heap))
    return ordenada


#MERGE SORT
def merge(A, aux, esquerda, meio, direita):
    """
    Combina dois vetores ordenados em um único vetor (também ordenado).
    """
    for k in range(esquerda, direita + 1):
        aux[k] = A[k]
    i = esquerda
    j = meio + 1
    for k in range(esquerda, direita + 1):
        if i > meio:
            A[k] = aux[j]
            j += 1
        elif j > direita:
            A[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            A[k] = aux[j]
            j += 1
        else:
            A[k] = aux[i]
            i += 1
'''
def mergesort(A, aux, esquerda, meio):
    aux = [0] * len(A)
    esquerda = 0
    direita = len(A) - 1
    if direita <= esquerda:
        return
    meio = (esquerda + direita) // 2

    # Ordena a primeira metade do arranjo.
    mergesort(A, aux, esquerda, meio)

    # Ordena a segunda metade do arranjo.
    mergesort(A, aux, meio + 1, direita)

    # Combina as duas metades ordenadas anteriormente.
    merge(A, aux, esquerda, meio, direita)
'''

def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


