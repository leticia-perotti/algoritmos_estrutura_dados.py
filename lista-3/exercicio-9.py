from pydoc import doc


b = bool
b = True
soma = 0

while b:
    entrada = input("Deseja digitar um valor s/n")

    if (entrada == 's'):
        valor = int(input('Digite um valor'))

        soma = soma + (valor * valor)
    elif (entrada == 'n'):
        print("A soma do quadrado é %d" %soma)
        b = False