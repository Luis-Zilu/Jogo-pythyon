import os

while True:
    os.system("cls")

    print("""
█▀█ ▄▀█ █▀█ █▄▀ █░█ █▀█ █▀▀ █ █▀█ █▀█   █▀▀ █▀▀ █▀▀ █▀     ▄██▄
█▀▀ █▀█ █▀▄ █░█ █▄█ █▀▄ ██▄ █ █▀▄ █▄█   ██▄ █▄█ █▄█ ▄█    ██████       
                                                          ▀████▀""")

    input("Aperte enter para começar: ")
    os.system("cls")

    print("Tente adivinhar em que andar o ovo sobrevive.")
    print("Você terá duas tentativas, boa sorte.\n")

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

        if 45 <= usuario <= 67:
            print("Ovo sobreviveu! Você venceu!")
            break
        else:
            print("Quebrou o ovo")

            if usuario < 45:
                print("É um número maior.")
            elif usuario > 67:
                print("É um número menor.")

        if tentativas == 2:
            print("CHANCE DECISIVA!")

        if tentativas == 3:
            print("Você perdeu.")
            break

    reiniciar = input("\nAperte ENTER para reiniciar ou digite 'sair' para finalizar: ").lower()

    if reiniciar == "sair":
        break