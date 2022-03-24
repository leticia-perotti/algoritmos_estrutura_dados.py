macas = int(input("Digite o número de maças compradas: "))

if (macas<12):
    valor = macas * 0.5
elif (macas>=12):
    valor = macas * 0.4

print("O valor total é de %.2f" % valor)