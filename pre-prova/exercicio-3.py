matriz = []

for i in range(3):
    lista = []
    for j in range(3):
        valor = int(input("Digite um valor"))
        lista.append(valor)
    matriz.append(lista)

vetor = []
soma = 0

for i in range(3):
    for j in range(3):
        soma = soma + matriz[i][j]
    vetor.append(soma)
    soma = 0

suporte = []

for i in range(3):
    if vetor[i] > 10:
        suporte.append(vetor[i])

if len(suporte):
    print(suporte)
else:
    print("Erro")

