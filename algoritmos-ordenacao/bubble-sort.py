lista = []
b = True

while b:
    opcao = (input("Deseja adicionar outro valor na lista? S/N "))

    if opcao == 'n' or opcao == 'N':
        b = False
    elif opcao == 'S' or opcao == 's':
        valor = int(input("Digite um valor"))
        lista.append(valor)
    else:
        print("Valor inválido")

#algoritmo bubble

tamanho = len(lista)
aux = lista[:]

for i in range(tamanho):
    for j in range(tamanho-i-1):
        if aux[j] > aux[j+1]:
            temp = aux[j]
            aux[j] = aux[j + 1]
            aux[j+1] = temp

print("Lista original: ")
print(lista)
print("Lista ordenada: ")
print(aux)