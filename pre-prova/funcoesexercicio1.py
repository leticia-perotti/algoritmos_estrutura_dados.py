import math

def parouimpar():
    valor = int(input('Digite um valor'))

    if valor % 2 == 0:
        return print('É par')
    elif valor % 2 != 0:
        return print('É impar')

def multiplicar():
    valor1 = int(input('Digite o primeiro valor'))
    valor2 = int(input('Digite o segundo valor'))

    resultado = valor1 * valor2

    return print('O resultado da multiplicação é %.2f' % resultado)

def dividir():
    valor1 = int(input('Digite o primeiro valor'))
    valor2 = int(input('Digite o segundo valor'))

    resultado = valor1 / valor2

    return print('O resultado da divisão é %.2f' % resultado)

def raiz():
    valor1 = int(input('Digite o valor'))

    resultado = math.sqrt(valor1)

    return print('A raiz quadrada é %.2f' % resultado)

