def insertion_sort(lista):
    y = len(lista)

    for i in range(1,y):
        chave = lista[i]
        j = i - 1
        while j>= 0 and lista[j]>chave:
            lista[j+1]= lista[j]
            j = j - 1
        lista[j+1] = chave
    return lista

lista = []
n = True

while n:
    opcao = (input("Deseja adicionar nome? S/N "))

    if opcao == 'n' or opcao == 'N':
        n = False
    elif opcao == 's' or opcao == 'S':
        valor = input("Digite um nome:")
        lista.append(valor)
    else:
        break
       

x=insertion_sort(lista)
print(x)

