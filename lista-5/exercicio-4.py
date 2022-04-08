matrizA = []
matrizB = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input("Digite um valor para primeira matriz"))
        linha.append(valor)

    matrizA.append(linha)

print('\n')

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input("Digite um valor para segunda matriz"))
        linha.append(valor)

    matrizB.append(linha)

matrizResult = []

for l in range(3):
    linha = []
    for c in range(3):
        valor = 0
        for k in range(3):
            valor = valor + (matrizA[l][k] * matrizB[k][c])
        linha.append(valor)     
    matrizResult.append(linha)

for i in range(3):
    print(matrizResult[i])

