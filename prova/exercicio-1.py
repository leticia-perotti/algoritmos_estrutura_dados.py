soma , impares = 0,0

for i in range(5):
    valor = int(input("Digite um valor"))
    soma = soma + valor

    if valor % 2 != 0:
        impares += 1

print("A soma dos valores é %.2f" % soma)
print("A quantidade de valores ímpares é %.2f" % impares)
