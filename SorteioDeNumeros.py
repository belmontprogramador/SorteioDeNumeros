# sorteio de numeros aleatorios #

import random
import os

def sorteio():
    numeroDaSorte = (int(input("Digite seu numero da Sorte de 1 a 100 ")))
    num = random.randrange(1,101)
    print(num)
    if numeroDaSorte == num:
        print("parabéns você foi o vencedor")
    elif numeroDaSorte != num:
        print(" desculpe não foi dessa vez tente de novo")

os.system("cls")

while True:
    sorteio()
    continuar = input ('deseja continuar (S/N)')
    if continuar == 'N' or continuar == 'n':
        os.system("cls")
        print('finalizando')
        break
    elif continuar == "s" or "S":
        os.system("cls")
        print('continuando')
    else:
        os.system("cls")
        print('ok vamos la!')