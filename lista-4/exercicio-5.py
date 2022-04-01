notas = [0] * 6

for i in range(0,6,1):
    valor = int(input("Digite um valor: "))
    notas[i] = valor

media = 0
soma = 0

for  i in range(0,6,1):
    soma = soma + notas[i]

media = soma / 6

print("O valor da média é %.2f" % media)