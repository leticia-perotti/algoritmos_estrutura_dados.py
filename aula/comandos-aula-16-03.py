#alterar tipo de variável

inteiro = int(input("Digite um valor"))
float = 2.2222
print ("Inteiro: %d e float: %.2f" % (inteiro, float))

#operadore

505 // 10 # a resposta é 50 

#random
import random

#exemplo 1
aleatorio = print(50 + random.random)

#exemplo 2
y = random.randint(3,9)

#----------------------------------------------------#
#if e else
#lembrar sempre de identar

nota = 5

if (nota>=7):
    print('aprovado')
elif (5<=nota<7):
    print('em recuperação')
else:
    print('reprovado')

# while

true = True
false = False

while (true):
    print('Isso é um loop infinito')

#for

#for i in range(inicio, fim, incremento):
for i in range(fim, incremento):
    print('for')

#i++
i+=1

# declara a lista
lista = []

#adiciona na lista
lista.append(n)

#tamanho da lista 
len(lista)

#concatenar lista
lista1 = [1,2]
lista1 = lista1 + [3,4,5]
#retorna 1 2 3 4 5 

#sei o tamanho da lista 
tamanho = 10
lista = [0] * tamanho

#se está na lista se
lista =[1,2,3]
resultado = 7 in lista #vai retornar false

#slip():
x = input("Digite os valores separados po /").split('/')
print(x) # isso forma uma lista

#pra copiar lista tem que usar o for
lista1 = [1,2,3]
lista2 = []

for i in range(len(lista1)):
    lista2.append(lista1[i])