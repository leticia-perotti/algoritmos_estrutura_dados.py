matriz = []
maior = 0
linhaMaior, colunaMaior = 0, 0

for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input("Digite um valor"))
        linha.append(valor)

        if valor > maior:
            maior = valor
            linhaMaior = j
            colunaMaior = i
    matriz.append(linha)
    linha = []

for i in range(4):
    print(matriz[i])

print("O maior valor é %d \nNa posição %d %d" % (maior, linhaMaior, colunaMaior))
