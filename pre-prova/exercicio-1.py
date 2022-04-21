from funcoesexercicio1 import *;

print("Menu de opções")
opcao = int(input('1. Ver se um número é par ou ímpar \n2. Multiplicar dois números\n3. Dividir dois números\n4. Raiz quadrada de um número\nDigite sua opção: '))

if opcao == 1:
    parouimpar();
elif opcao == 2:
    multiplicar();
elif opcao == 3:
    dividir();
elif opcao == 4:
    raiz();
else:
    print("Opção inválida!!!")
