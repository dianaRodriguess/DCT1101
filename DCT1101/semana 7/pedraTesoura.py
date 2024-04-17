import random

escolha = input("Quer Jorgar? S/N: ")

while escolha.lower() == "s":
    print()
    jogador = int(input("Escolha de acordo: 1-Pedra; 2-Papel; 3-Tesoura: "))

    ppt = {"Pedra": 1, "Papel": 2, "Tesoura": 3}
    name, id = random.choice(list(ppt.items()))

    if (jogador == 1):
        if (id == 3):
            print("Jogador Ganhou!!")
        elif (id == 2):
            print("Jogador Perdeu!!")
        else:
            print("Empate!!")
    elif (jogador == 2):
        if (id == 1):
            print("Jogador Ganhou!!")
        elif (id == 3):
            print("Jogador Perdeu!!")
        else:
            print("Empate!!")
    else:
        if (id == 2):
            print("Jogador Ganhou!!")
        elif (id == 1):
            print("Jogador Perdeu!!")
        else:
            print("Empate!!")
    # print(jogador, id)
    print()
    for key, value in ppt.items():
        if jogador == value:
            print("Jogador: ", key)
        if id == value:
            print("Computador: ", key)
    escolha = input("Quer continuar jogando? S/N: ")


# dic = {'Pedro': 99, 'João': 19, 'Rosa': 35, 'Maria': 23}
# name, id = random.choice(list(dic.items()))
