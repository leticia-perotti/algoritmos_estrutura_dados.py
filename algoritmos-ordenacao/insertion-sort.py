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

for i in range(1, tamanho):
    chave = lista[i]
    j = i - 1
    while j >= 0 and chave < aux[j]:
        aux[j + 1] = aux[j]
        j -= 1
        aux[j + 1] = chave

print("Lista original: ")
print(lista)
print("Lista ordenada: ")
print(aux)