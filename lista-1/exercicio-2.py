watts = float(input("Digite a potência da lâmpada"))
largura = float(input("Digite a largura do comodo"))
comprimento = float(input("Digite o comprimento do comodo"))

area = comprimento * largura;
lampadas = area * 18 / watts;

print ("O número de lâmpadas necessária é", lampadas)