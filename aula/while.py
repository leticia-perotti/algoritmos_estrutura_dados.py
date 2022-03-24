import random

valor = int(input('Digite um valor'))
soma=0
loop = bool

while loop :
    aleatorio = random.randint(1,10)
    print(aleatorio)
    soma = soma + aleatorio

    if(valor == aleatorio):
        print('Deu certo!')
        print('\n A soma é %d' % (soma))
        loop = False


