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