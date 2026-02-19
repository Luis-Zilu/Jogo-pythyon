import os
os.system("cls")
print("""
█▀█ ▄▀█ █▀█ █▄▀ █░█ █▀█ █▀▀ █ █▀█ █▀█   █▀▀ █▀▀ █▀▀ █▀     ▄██▄
█▀▀ █▀█ █▀▄ █░█ █▄█ █▀▄ ██▄ █ █▀▄ █▄█   ██▄ █▄█ █▄█ ▄█    ██████       
                                                          ▀████▀""")
comecar = input("Aperte enter para começar: ")
os.system("cls")
comecar = "enter"
tentativas = 0
condicao = True
while condicao:
    print("Tente adivinhar em que andar o ovo quebra. Você terá duas tentativas, boa sorte.")
    usuario = int(input("Digite um andar de 1 a 100 para arremessar seu ovo: "))
    if usuario >= 45 and usuario <= 67:
        print("Ovo sobreviveu.")
        break
    elif usuario == 0:
        os.system("cls")
        print("Tu é beta! Hahaha")
        continue
    elif tentativas<=1:
        print("Quebrou o ovo")
        os.system("cls")
    if tentativas == 2:
        condicao = False
    tentativas +=1
    if usuario < 45:
        print("É um número maior.")
    elif usuario > 67:
        print("É um número menor.")
    if tentativas == 2:
        print("CHANCE DECISIVA!")
