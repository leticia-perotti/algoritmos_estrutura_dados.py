b = bool
b = True

while b :
    print("Opções \n 1. Somar \n 2.Subtrair \n 3.Dividir \n 4.Multiplicar \n 5.Sair")

    operacao = int(input("Digite o numero da operação que deseja realizar"))

    if (operacao == 5):
        print("Fim do programa")
        b = False
    elif (operacao == 1 or operacao == 2 or operacao == 3 or operacao == 4):
        valor1 = int(input("Digite o primeiro valor"))
        valor2 = int(input("Digite o segundo valor"))

        if(operacao == 1):
            soma = valor1 + valor2
            print("O valor da soma é %d" % soma)
        elif(operacao == 2):
            subtrair = valor1 - valor2
            print("O valor da subtração é %d" % subtrair)
        elif(operacao == 3):
            dividir = valor1 / valor2
            print("O valor da divisão é %d" %dividir)
        elif(operacao == 4):
            multiplicar = valor1 * valor2
            print("O valor da multiplicação é %d" % multiplicar)
