from re import L


lista = [0] * 5

for i in range(0,5,1):
    valor = int(input("Digite um valor: "))
    lista[i] = valor

digitado = int(input("Digite um valor X: "))
existe = digitado in lista
posicao = 0

if existe:
    for i in range(0,5,1):
        if lista[i] == digitado:
            posicao = i
    print("\n A posição do valor digitado é %d" % posicao)
else:
    print("-1")
