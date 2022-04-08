matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input("Digite um valor para matriz"))
        linha.append(valor)
    matriz.append(linha)

print('\n')

matrizResult = []

for l in range(3):
    linha = []
    for c in range(3):
        valor = 0
        for k in range(3):
            valor = valor + (matriz[l][k] * matriz[k][c])
        linha.append(valor)     
    matrizResult.append(linha)

for i in range(3):
    print(matrizResult[i])

