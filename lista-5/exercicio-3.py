matriz1 = []
matriz2 = []

for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input("Digite um valor para primeira matriz"))
        linha.append(valor)

    matriz1.append(linha)


for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input("Digite um valor para segunda matriz"))
        linha.append(valor)

    matriz2.append(linha)

matrizResult = []

for i in range(4):
    linha = []
    for j in range(4):
        if matriz1[i][j] > matriz2[i][j]:
            linha.append(matriz1[i][j])
        elif matriz1[i][j] < matriz2[i][j]:
            linha.append(matriz2[i][j])
        elif matriz1[i][j] == matriz2[i][j]:
            linha.append(matriz2[i][j])
    
    matrizResult.append(linha)


for i in range(4):
    print(matrizResult[i])