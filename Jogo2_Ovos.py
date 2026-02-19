<<<<<<< Updated upstream
tentativas = 1
condicao = True
while condicao:
    print("Tente adivinhar em que andar o ovo quebra. Você terá duas tentativas, boa sorte.")
    usuario = int(input("Digite um andar de 1 a 100 para arremessar seu ovo: "))
    if usuario >= 15 and usuario <= 50:
        print("Ovo sobreviveu")
        break
    elif usuario == 0:
        print("Engana outro, mas não eu.")
        continue
    else:
        print("Wasted.")
    if tentativas == 2:
        condicao = False
    tentativas +=1
=======
import os
os.system("cls")
print("""
█▀█ ▄▀█ █▀█ █▄▀ █░█ █▀█ █▀▀ █ █▀█ █▀█   █▀▀ █▀▀ █▀▀ █▀
█▀▀ █▀█ █▀▄ █░█ █▄█ █▀▄ ██▄ █ █▀▄ █▄█   ██▄ █▄█ █▄█ ▄█""")
comecar = input("Aperte enter para começar: ")
os.system("cls")
comecar = "enter"
>>>>>>> Stashed changes
