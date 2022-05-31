lista1 = []
lista2 = []

b, c = True, True

while b:
    print('Incluir mais um valor na lista 1? S/N')
    resposta = input('Opcao')

    if resposta == 'n' or resposta == 'N':
        b = False
    elif resposta == 's' or resposta == 'S':
        valor = int(input('Digite um valor'))
        lista1.append(valor)
    else:
        print('Opção incorreta')
while c:
    print('Incluir mais um valor na lista 2? S/N')
    resposta = input('Opcao')

    if resposta == 'n' or resposta == 'N':
        c = False
    else:
        valor = int(input('Digite um valor'))
        lista2.append(valor)

lista3 = []
copy = []

if len(lista1) > len(lista2):
    copy = lista1
    for i in range(len(lista2)):
        lista3.append(lista2[i])
        lista3.append(lista1[i])
        copy.pop(i)
    lista3.extend(copy)
    
else:
    copy = lista2
    for i in range(len(lista1)):
        lista3.append(lista1[i])
        lista3.append(lista2[i])
        copy.pop(i)
    lista3.extend(copy)

print(lista3)
