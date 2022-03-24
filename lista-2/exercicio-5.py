#lado1 = float(input("Digite o valor do lado 1: "))
#lado2 = float(input("Digite o valor do lado 2: "))
#lado3 = float(input("Digite o valor do lado 3: "))

import math

lado1X = float(input("Digite a coordenada X do priemiro ponto"))
lado1Y = float(input("Digite a coordenada Y do priemiro ponto"))

lado2X = float(input("Digite a coordenada X do segundo ponto"))
lado2Y = float(input("Digite a coordenada Y do segundo ponto"))

lado3X = float(input("Digite a coordenada X do terceiro ponto"))
lado3Y = float(input("Digite a coordenada Y do terceiro ponto"))

lado1 = ((lado1X - lado2X) *(lado1X - lado2X)) + ((lado1Y - lado2Y) *(lado1Y - lado2Y))
lado1 = math.sqrt(lado1)

lado2 = ((lado1X - lado3X) *(lado1X - lado3X)) + ((lado1Y - lado3Y) *(lado1Y - lado3Y))
lado2 = math.sqrt(lado2)

lado3 = ((lado2X - lado3X) *(lado2X - lado3X)) + ((lado2Y - lado3Y) *(lado2Y - lado3Y))
lado3 = math.sqrt(lado3)


if(lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1):
    print("Os 3 lados formam um triangulo!\n")

    if(lado1 == lado2 and lado1 == lado3 and lado3 == lado2):
        print("O triângulo é equilatero");
    elif(lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
        print("O triângulo é isóceles")
    elif(lado1 != lado2 and lado1 != lado3 and lado2 != lado3):
        print("O triângulo é escaleno")
    
else:
    print("Isso não forma um triângulo")

#Perguntar se era assim a execução, pois ele pedia a coordeanda dos pontos, apartir disto teria que calcular
#a distância entre os pontos para saber, e apartir disso calcular os lados
# formula da distância dAB² = (xB – xA)² + (yB – yA)²
