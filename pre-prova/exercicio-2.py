import random

numeroMagico = random.randint(0, 250)
b = bool
b = True
erro = 0
print(numeroMagico)
while b:
    valor = int(input('Digite um valor'))

    if valor != numeroMagico:
        erro += 1
        if valor > numeroMagico:
            print('Errou! Maior que o número mágico')
        elif valor < numeroMagico:
            print('Errou! Menor que o número mágico')
    elif valor == numeroMagico:
        #print(erro)
        if erro <= 3:
            print('Acertou')
            print('Você é muito sortudo')
            b = False
        elif (erro >= 4) and (erro <= 6):
            print('Acertou')
            print('Você é sortudo')
            b = False
        elif (erro >= 7) and (erro <= 10):
            print('Acertou')
            print('Você é normal') 
            b = False
        elif erro > 10:
            print('Acertou')
            print('Azarado! Tente novamente')
            b = False