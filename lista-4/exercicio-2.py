lista = [0] * 5

for i in range(0,5,1):
    valor = int(input("Digite um valor: "))
    lista[i] = valor

maior = 0
menor = 999999999999999999
soma = 0

for i in range(len(lista)):
    if lista[i] > maior:
        maior = lista[i]
    if lista[i] < menor:
        menor = lista[i]
    
soma = maior + menor
print("A soma é %d" % soma)