valor = 0
pares = 0
impares = 0
i =0

while i<10:
    i = i + 1

    valor = float(input("Digite um valor"))

    if (valor % 2 == 0):
        pares = pares + 1
    else:
        impares = impares + 1

print("Pares: %d" % pares)
print("\nImpares: %d" %impares)