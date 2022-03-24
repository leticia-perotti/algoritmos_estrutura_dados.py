codigo = int(input("Digite a região de origem do produto "))

if (codigo == 1):
    print("Região sul")
elif (codigo == 2):
    print("Região norte")
elif (codigo == 3):
    print("Região leste")
elif (codigo == 4):
    print("Região oeste")
elif (codigo == 5 or codigo == 6):
    print("Região nordeste")
elif (codigo == 7 or codigo == 8 or codigo == 9):
    print("Região sudeste")
elif (codigo == 10):
    print("Região centro-oeste")
elif (codigo == 11):
    print("Região noroeste")
else:
    print("Produto importado")