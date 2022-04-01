lista = [0] * 10

for i in range(0,10,1):
    valor = int(input("Digite um valor: "))
    lista[i] = valor

diferente = 0
suporte = []

for i in range(0,10,1):
    #for j in range(0,i,1):
        #if i == 0:
           # suporte.append(lista[i])
        #else:
            resultado = lista[i] in suporte 
            if resultado != True:
                diferente += 1
                suporte.append(lista[i])

quantidade = len(suporte)

print(suporte)
print("\n")
print("O número de valores diferentes é %d" %diferente)