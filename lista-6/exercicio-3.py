from funcoesPerimetroArea import areaCircunferencia, perimetroCircunferencia, areaRetangulo, perimetroRetangulo, areaTrianguloEquilatero, perimetroTrianguloEquilatero

def circunferencia():
    raio = int(input("Digite o valor do raio"))
    print("A área é" , areaCircunferencia(raio))
    print("O perímetro é" , perimetroCircunferencia(raio))
    return 0

def triangulo():
    lado = int(input("Digite o lado do triangulo equilatero"))
    print("A área é =~" , areaTrianguloEquilatero(lado))
    print("O perímetro é " , perimetroTrianguloEquilatero(lado))
    return 0

def retangulo():
    base = int(input("Digite a área da base"))
    altura = int(input("Digite a altura"))
    print("A área é" , areaRetangulo(base, altura))
    print("O perímetro é" , perimetroRetangulo(base, altura))
    return 0

    

print("1-Circunferência \n2-Triângulo Equilátero \n3-Retângulo")
tipo = int(input("Digite o tipo de figura que deseja ler"))

if tipo == 1:
    circunferencia()
elif tipo == 2:
    triangulo()
elif tipo == 3:
    retangulo()
