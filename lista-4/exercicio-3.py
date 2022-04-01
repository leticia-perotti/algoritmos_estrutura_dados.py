tupla = ()
for i in range(0,10,1):
    valor = int(input("Digite um valor: "))
    tupla = tupla + (valor,)

maior = 0 
posicao = 0

for i in range(len(tupla)):
    if tupla[i] > maior:
        maior = tupla[i]
        posicao = i

print(tupla)
print("O maior valor é %.2f, que está na posição %.2f" % (maior, posicao))