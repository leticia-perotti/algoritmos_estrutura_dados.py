lista = [0] * 5

for i in range(0,5,1):
    valor = int(input("Digite um valor"))
    lista[i] = valor

maior, posicaoMaior = 0, 0
menor, posicaoMenor = 999999999999999, 0

for i in range(0,5,1):
    if lista[i] > maior:
        maior = lista[i]
        posicaoMaior = i
    if lista[i] < menor:
        menor = lista[i]
        posicaoMenor = i

print('O maior valor é %d, na posição %d \n O menor valor é %d, na posição %d' % (maior, posicaoMaior, menor, posicaoMenor))

