lista = []
listaPares = []

par = 0

for i in range(0,7,1):
    valor = int(input("Digite um valor: "))
    lista.append(valor)

for i in range(len(lista)):
    if (lista[i] % 2 == 0):
        par += 1
        listaPares.append(lista[i])

print("A quantidade de números pares é %d \n a seguir a lista de pares" % par)
print(listaPares)