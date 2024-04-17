from random import randint

escolha = input("Quer jogar?0 S/N: ")

while escolha.lower() == "s":
    print("----------Começo do jogo----------")
    comp1 = randint(0,1)
    comp2 = randint(0,1)

    jogador = int(input("0(Zero) ou 1(Um)? "))

    if (jogador != comp1) and (jogador != comp2):
        print("Jogador Ganhou!!")
    elif (comp1 != jogador) and (comp1 != comp2):
        print("Computador 1 Ganhou!!")
    elif (comp2 != jogador) and (comp2 != comp1):
        print("Computador 2 Ganhou!!")
    else:
        print("Empate!!")
        escolha = input("Quer jogar novamente? S/N: ")
    print("----------Fim do jogo----------")

