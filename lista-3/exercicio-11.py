b = bool
b = True

salario = 0
time = 0
cidade = 0
flamengo = 0
vasco = 0
fluminense = 0 
botafogo = 0
outro = 0
entrevistados = 0
somaSalarioFlamengo, somaSalarioVasco, somaSalarioFluminense, somaSalarioBotafogo = 0, 0, 0, 0
mediaSalarioFlamengo, mediaSalarioVasco, mediaSalarioFluminense, mediaSalarioBotafogo = 0, 0, 0, 0

while b:
    print("\n Bem vindo! \n Opções \n 1 . Cadastrar novo dado \n 2 . Ver dados coletados \n 3 . Sair do sistema")
    opcao = int(input("Digite a opção escolhida"))

    if (opcao == 1):
        entrevistados = entrevistados + 1
        print("Qual seu clube de prefencia? \n 1 – Flamengo \n 2 – Vasco \n 3 – Fluminense \n 4 – Botafogo \n 5 – Outros")
        clube = int(input("Digite sua opção: "))

        salario = float(input("Qual o valor do seu salário"))

        print("Qual sua cidade natal? \n 1 . Niterói \n 2 . Outra")
        cidade = int(input("Digite sua opção: "))

        if (clube == 1):
            flamengo = flamengo + 1
            somaSalarioFlamengo = somaSalarioFlamengo + salario
            mediaSalarioFlamengo = somaSalarioFlamengo / flamengo
        elif (clube == 2):
            vasco = vasco + 1
            somaSalarioVasco = somaSalarioVasco + salario
            mediaSalarioVasco = somaSalarioVasco / vasco
        elif (clube == 3):
            fluminense = fluminense + 1
            somaSalarioFluminense = somaSalarioFluminense + salario
            mediaSalarioFluminense = somaSalarioFluminense / fluminense
        elif (clube == 4):
            botafogo = botafogo + 1
            somaSalarioBotafogo = somaSalarioBotafogo + salario
            mediaSalarioBotafogo = somaSalarioBotafogo / botafogo
        elif (clube == 5 and cidade == 1):
            outro = outro + 1

    if(opcao == 2 ):
        
        print("         Número de torcedores | media salarial\n")
        print("Flamengo     %d               |   % d" %(flamengo,mediaSalarioFlamengo))
        print("Vasco        %d               |   % d" %(vasco,mediaSalarioVasco))
        print("Fluminense   %d               |   % d" %(fluminense,mediaSalarioFluminense))
        print("Botafogo     %d               |   % d" %(botafogo,mediaSalarioBotafogo))
        print("********************************************************")
        print("O número total de pessoas entrevistadas é de %d" %(entrevistados))
        print("O número total de pessoas nascidas em Niterói e que não torcem para nenhum dos principais clubes do Rio é %d" % outro)

    if ( opcao == 3 ):
        print("Você saiu do sistema!")
        b = False

