import os
import random

andar = random.randint(1,100)

while True:
    os.system("cls")

    print("""
█▀█ ▄▀█ █▀█ █▄▀ █░█ █▀█ █▀▀ █ █▀█ █▀█   █▀▀ █▀▀ █▀▀ █▀     ▄██▄    ▄██▄
█▀▀ █▀█ █▀▄ █░█ █▄█ █▀▄ ██▄ █ █▀▄ █▄█   ██▄ █▄█ █▄█ ▄█    ██████  ██████       
                                                          ▀████▀  ▀████▀""")

    input("Aperte enter para começar: ")
    os.system("cls")

    print("Tente adivinhar em que andar o ovo sobrevive.")
    print("Você terá dois ovos com 10 tentativas, boa sorte.\n")

    tentativas = 0
    condicao = True

    while condicao:
        try:
            usuario = int(input("Digite um andar de 1 a 100 para arremessar seu ovo: "))
            os.system("cls")
        except ValueError:
            print("Digite apenas números.")
            continue

        if usuario == 0:
            os.system("cls")
            print("Tu é beta! Hahaha")
            continue

        tentativas += 1

        if usuario == andar:
            print("Ovo sobreviveu! Você venceu!")
            break
        else:
            print("Quebrou o ovo🍳")

            if usuario < andar:
                print("É um número maior.")
            elif usuario > andar:
                print("É um número menor.")

        if tentativas == 9 or tentativas == 19:
            print("CHANCE DECISIVA!")

        if tentativas == 10:
            print("Quebrou o primeiro ovo.")
        if tentativas == 20:
            print("Game over.")
            break