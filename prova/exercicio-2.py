def diaSemana(dia):
    if dia == 0:
        return print("O melhor dia foi Segunda")
    elif dia == 1:
        return print("O melhor dia foi Terça")
    elif dia == 2:
        return print("O melhor dia foi Quarta")
    elif dia == 3:
        return print("O melhor dia foi Quinta")
    elif dia == 4:
        return print("O melhor dia foi Sexta")
    elif dia == 5:
        return print("O melhor dia foi Sábado")

semana = []
maiorVendaDia = 0
maiorVenda = 0
for i in range(6):
    quantidadeDiscos = int(input("Digite a quantidade de discos "))
    semana.append(quantidadeDiscos)

    if quantidadeDiscos > maiorVenda:
        maiorVenda = quantidadeDiscos
        maiorVendaDia = i

diaSemana(maiorVendaDia);
print("A quantidades de discos vendidos no dia foi de %.2f" % maiorVenda)