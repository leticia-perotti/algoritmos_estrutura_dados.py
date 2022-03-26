nuggets = int(input("Digite o numero de nuggets"))
controla = nuggets

while controla>5:
    if (controla >= 20):
        while (controla>= 20 and controla%6 != 0 and controla%9 != 0):
            controla = controla - 20
            #print(controla)

    if (controla >= 9):    
        while (controla>= 9 and controla%6 != 0):
            controla = controla - 9
           # print(controla)
    
    if (controla >= 6):
        while (controla>= 6):
            controla = controla - 6
            #print(controla)
    
if (controla == 0):
    print("TRUE, é possível comprar lanches nesta lanchonete")
else:
    print("FALSE, não é possível comprar lanches nesta lanchonete")
