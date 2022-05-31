import random

aleatorio = []

for i in range(10):
    aleatorio.insert(i, random.randint(1,6))

valoresObtidos = []

for i in range(1, 7):
    qtd = aleatorio.count(i)
    valoresObtidos.append(qtd)

print(aleatorio)
print(valoresObtidos)