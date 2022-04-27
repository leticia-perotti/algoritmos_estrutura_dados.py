lista = []
somaMenores = 0
maior, menor, iMaior, iMenor = 0,99999999999999999999,0,0

for i in range(4):
    valor = int(input("Digite um valor"))
    lista.append(valor)
    
    if valor <5:
        somaMenores = somaMenores + valor
    
    if valor > maior:
        iMaior = i
        maior = valor
    if valor < menor:
        iMenor = i
        menor = valor
    
soma2 = lista[1] + lista[3]

print(lista)
print("A soma dos valores menores que 5 é %.2f" %somaMenores)
print("O índice do menor é %d" %iMenor)
print("O índice do maior é %d" %iMaior)
print("A soma do segundo com o último é %d" %soma2)