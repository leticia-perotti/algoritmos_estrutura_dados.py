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


'''def particao(lista, inicio, fim):

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
    return lista'''
 
 
def quick(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

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
