matriz = []
maior = 0
maiores = 0

for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input("Digite um valor"))
        linha.append(valor)

        if valor >= 10:
            maiores += 1

    matriz.append(linha)
    linha = []

for i in range(4):
    print(matriz[i])

print("O existem %d maiores que 10" % (maiores))