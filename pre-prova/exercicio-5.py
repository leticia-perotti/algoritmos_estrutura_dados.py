import random
lista = []
b, c = bool, bool
b= True
c = True
suporte = []
contador = 0
k, j = 0, 0
repetido = bool
repetido = True

while b:
    if repetido:
            lista = []
            for i in range(5):
                valor = random.randint(1,10)
                lista.append(valor)
            #print(lista)
            repetido = False
    elif lista != []:
            b = False
    
    for k in range(5):
        for j in range(5):
            if ((lista[k] == lista[j]) and (k != j) and repetido == False):
                suporte.append(lista)
                contador += 1
                repetido = True              
    
if contador != 0:
        print('A quantidade de listas erradas é \n')
        print(contador)
        print('A lista correta é:\n')
        print(lista)
        print('As listas repetidas são \n')
        for i in range(contador):
            print(suporte[i])
      
else:
        print(lista)
       




