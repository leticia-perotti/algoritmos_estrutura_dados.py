from time import perf_counter
from AlgoritmosOrdenacaoGrupo0 import CombSort,heap_sort,mergesort
from AlgoritmosOrdenacaoGrupo1 import bubbleSort,insertion_sort,quick,shell_sort
from AlgoritmoOrdencaoSalaDeAula import selectionSort
from criarLista import gerarLista

listaValores = gerarLista()
contador = 1000
for i in range(len(listaValores)):
    lista = []
    inicio = perf_counter()
    lista = mergesort(listaValores[i])
    end = perf_counter()
    tempo = end - inicio

    if contador ==1000:
        print('mergesort '+str(contador)+" :",tempo)
        contador=contador*10
    else:
        print('mergesort '+str(contador)+" :",tempo)
        contador=contador*10












