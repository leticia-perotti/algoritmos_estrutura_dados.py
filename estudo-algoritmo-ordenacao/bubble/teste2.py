import sys
sys.path.insert(1,'./')

from time import perf_counter
from  AlgoritmosOrdenacaoGrupo1 import bubbleSort
from criarLista import gerarLista
from ordenarLista import cenario2

listaValores = gerarLista()
contador = 1000
for i in range(len(listaValores)):
    lista2 = cenario2(contador)
    lista = []
    inicio = perf_counter()
    lista = bubbleSort(lista2)
    end = perf_counter()
    tempo = end - inicio
   
    if contador ==1000:
        print('Bubble '+str(contador)+" :",tempo)
        contador=contador*10
    else:
        print('Bubble '+str(contador)+" :",tempo)
        contador=contador*10
