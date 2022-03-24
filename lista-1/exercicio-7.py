inicioDia = int(input(" Digite a marcação no inicio do dia: "))
fimDia = int(input("Digite a marcação no final do dia: "))
litrosGastos = float(input("A quantidade de litros gastos: "))
valorRecebido = float(input("Valor recebido: "))

mediaKmL = (fimDia - inicioDia)/litrosGastos;
valor = litrosGastos * 1.9;
valorTotal = valorRecebido - valor;

print("A média foi de %.2f e o lucro de %.2f" % (mediaKmL,valorTotal))