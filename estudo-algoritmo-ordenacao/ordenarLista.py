import random

def cenario1(lista): 
    lista2 = random.sample(lista, len(lista))
    return lista2

def cenario2(qtdPosicoes): 
    listaRandom = [] * qtdPosicoes
    for i in range(qtdPosicoes):
        listaRandom.append(random.randint(1,qtdPosicoes))
    return listaRandom

def cenario3(lista):
    ultimo =len(lista) -1
    lista[0] = lista[ultimo] 
    lista.pop()
    return lista

def cenario4(lista):
    lista.sort(reverse=True)
    return lista

lista = [0,1,2,3,4,5,6,7,8,9,10]
