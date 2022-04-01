import random

dado = [0] * 50

for i in range(0,50,1):
    valor = random.randint(1,6)
    dado[i] = valor

contadorSeis = 0

for i in range(0,50,1):
    if (dado[i] == 6):
        contadorSeis += 1

print(dado)
#print(contadorSeis)

percentual = (contadorSeis / 50) * 100
print("O percentual de números 6 é %.2f" %percentual)

