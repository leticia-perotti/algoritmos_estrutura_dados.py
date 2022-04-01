lista = [0] *6

for i in range(0,6,1):
    valor = int(input("Digite um valor: "))
    lista[i] = valor


for i in range(5,-1,-1):
    print(lista[i])