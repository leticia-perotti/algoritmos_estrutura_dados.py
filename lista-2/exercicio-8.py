dia = int(input('Digite o dia de seu aniversário'))
mes = int(input('Digite o mes de seu aniversário'))

if ((dia>= 21 and mes==3) or (dia<21 and mes== 4)):
    print('Seu signo é áries')
elif ((dia>= 21 and mes==4) or (dia<21 and mes== 5)):
    print('Seu signo é touros')
elif ((dia>= 21 and mes==5) or (dia<21 and mes== 6)):
    print('Seu signo é gêmeos')
elif ((dia>= 21 and mes==6) or (dia<23 and mes== 7)):
    print('Seu signo é câncer')
elif ((dia>= 23 and mes==7) or (dia<23 and mes== 8)):
    print('Seu signo é leão')
elif ((dia>= 23 and mes==8) or (dia<23 and mes== 9)):
    print('Seu signo é virgem')
elif ((dia>= 23 and mes==9) or (dia<23 and mes== 10)):
    print('Seu signo é libra')
elif ((dia>= 23 and mes==10) or (dia<22 and mes== 11)):
    print('Seu signo é escorpião')
elif ((dia>= 22 and mes==11) or (dia<22 and mes== 12)):
    print('Seu signo é sagitário')
elif ((dia>= 22 and mes==12) or (dia<21 and mes== 1)):
    print('Seu signo é capricórnio')
elif ((dia>= 21 and mes==1) or (dia<19 and mes== 2)):
    print('Seu signo é aquário')
elif ((dia>= 19 and mes==2) or (dia<21 and mes== 3)):
    print('Seu signo é peixes')
else:
    print('Data inválida')