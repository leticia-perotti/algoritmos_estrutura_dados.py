codigo = 0
matrizProfessores = []
homens , mulheres = 0,0
somaMulheres, mediaMulheres, somaHomens, mediaHomens = 0,0, 0, 0
linhasNum = 0

while codigo != 99999:
    codigo = int(input('Digite o codigo '))
    if codigo == 99999:
        break
    linha = []
    for i in range(1):
        sexo = input('O sexo é M para masculino ou F para feminino? ')
        numeroHorasAula = int(input('Digite o número de horas aula '))

        salarioBruto = numeroHorasAula * 30

        if sexo =='M' or sexo =='m':
            salarioLiquido = salarioBruto - ((salarioBruto / 100) * 10)
            homens += 1
            somaHomens = somaHomens + salarioLiquido
            mediaHomens = somaHomens / homens
        elif sexo =='F' or sexo =='f':
            salarioLiquido = salarioBruto - ((salarioBruto / 100) * 5)
            mulheres += 1
            somaMulheres = somaMulheres + salarioLiquido
            mediaMulheres = somaMulheres / mulheres
        
        linha.append(codigo)
        linha.append(salarioBruto)
        linha.append(salarioLiquido)
        
    #print(linha)
    matrizProfessores.append(linha)
    linhasNum += 1


for i in range(linhasNum):
    print(matrizProfessores[i])

print('A média de salários masculinos é %.2f' % mediaHomens)
print('A média de salários femininos é %.2f' % mediaMulheres)