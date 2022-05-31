lista = []
aux = []

b = True
total = 0
timeMais, timeMenos = '', ''
maior = 0
menor = 99999

while b:
    print('Incluir mais um valor na lista s/n')
    resposta = input('Digite sua opcao ')

    if resposta == 'n' or resposta == 'N':
        b = False
    elif resposta == 's' or resposta == 'S':
        pais1 = input('Digite o primeiro país ')
        pais2 = input('Digite o segundo país ')
        valor1 = int(input('Digite as faltas do país 1 '))
        valor2 = int(input('Digite as faltas do país 2 '))
        total = total + valor1 + valor2

        if valor1 > maior:
            maior = valor1
            timeMais = pais1
        if valor1 < menor:
            menor = valor1
            timeMenos = pais1
        
        if valor2 > maior:
            maior = valor2
            timeMais = pais2
        if valor2 < menor:
            menor = valor2
            timeMenos = pais2

        lista.append([pais1, pais2, [valor1, valor2]])
    else:
        print('Opção incorreta')

print(lista)
print('O total de faltas é ' + str(total))
print('O time que fez menos faltas é ' + str(timeMenos))
print('O time que fez mais faltas é ' + str(timeMais))