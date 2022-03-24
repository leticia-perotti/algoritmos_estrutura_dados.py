nome = input("Digite o nome do produto:")
quantidade = int(input("Quantidade comprada:"))
valorUnidade = float(input("Valor da unidade:"))
desconto = int(input("Desconto aplicado (exemplo 50, para 50%):"))

total = valorUnidade * quantidade;
total = total - ((total/100) * desconto);

print("O valor total da venda do produto %s é de %.2f" % (nome, total))