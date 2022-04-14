def mes_ano(num_mes):
    if (num_mes == 1):
        return print("Janeiro")
    elif (num_mes == 2):
        return print("Fevereiro")
    elif (num_mes == 3):
        return print("Março")
    elif (num_mes == 4):
        return print("Abril")
    elif (num_mes == 5):
        return print("Maio")
    elif (num_mes == 6):
        return print("Junho")
    elif (num_mes == 7):
        return print("Julho")
    elif (num_mes == 8):
        return print("Agosto")
    elif (num_mes == 9):
        return print("Setembro")
    elif (num_mes == 10):
        return print("Outubro")
    elif (num_mes == 11):
        return print("Novembro")
    elif (num_mes == 12):
        return print("Dezembro")
    else:
        return print("ERRO")

numero = int(input("Digite um valor"))
mes_ano(numero)