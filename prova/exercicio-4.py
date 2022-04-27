matriz = []
maior = 0
menor = 999999999999999999
pares = 0


for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input("Digite um valor"))
        linha.append(valor)

        if valor > maior:
            maior = valor
        if valor <menor:
            menor = valor
        
        if valor% 2 == 0:
            pares += 1

    matriz.append(linha)

for i in range(3):
    print(matriz[i])

print('O maior valor é %d' % maior)
print('O menor valor é %d' % menor)
print('A quantidade de valores pares é %d' %pares)
        