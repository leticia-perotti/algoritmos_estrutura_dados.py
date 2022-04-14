def status(media):
    if media >= 6:
        return print("Aprovado")
    elif 6>media>=4:
        return print("Verificação Suplementar")
    elif media<4:
        return print("Reprovado")

def mediaCalc():
    nota1 = int(input("Digite nota 1"))
    nota2 = int(input("Digite nota 2"))
    media = (nota1+ nota2)/2
    return status(media)
    
mediaCalc()
