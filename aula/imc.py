massa = float(input("Digite seu peso em kg "));
altura = float(input("Digite sua altura "));

imc = massa / (altura * altura)

if (imc<18.5):
    print("Você está abaixo do peso")
elif (18.5<imc<25):
    print("Você está saudável")
elif (25<imc<30):
    print("Você está acima do peso")
elif (30<imc<35):
    print("Você está em obesidade grau I")
elif(35<imc<40):
    print("Você está em obesidade grau II")
elif(imc>=40):
    print("Você está em obesidade grau III")
else:
    print("Erro!")
