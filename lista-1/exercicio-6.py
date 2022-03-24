from re import I


comprimento = float(input("Digite o valor comprimento (em M)"))
larguna = float(input("Digite o valor da largura"))
altura = float(input("Digite o valor da altura"))

parede1 = comprimento * altura;
parede2 = larguna * altura;

total = (parede1 * 2) + (parede2 * 2)
total = total / 1.5

print("Serão necessário %.2f caixas de azulejos" % total)