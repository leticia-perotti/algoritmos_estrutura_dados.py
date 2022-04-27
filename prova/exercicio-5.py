b = bool
b = True
soma, media, num = 0,0,0

while b:
    valor = int(input("Digite um valor"))

    if valor == 0:
        b = False
    else:    
        num += 1
        soma = soma + valor
        media = soma / num

print('A soma é %d' % soma)
print('A média é %.2f' % media)