inicio = int(input('Digite o inicio do intervalo: '))
fim = int(input('Digite o fim do intervalo: '))

soma = 0

for i in range(inicio, fim, 1):
    soma = soma + i
    #print(soma)

print('A soma total é %d' % soma)
#aqui o fim do intervalo não entra na soma