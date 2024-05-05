from random import randint

escolha = input("Quer jogar esse jogo incrivel que demorou anos para ser desenvolvido? Sim - S Não - N: ")
    
while escolha.upper() == "S":
    print("Começo do jogo")
    dado1 = randint(1,6)
    dado2 = randint(1,6)

    soma_dados = dado1 + dado2
    
    if (soma_dados == 7) or (soma_dados == 11):
        print("-"*15)
        print("Jogador Gannhou!!")
        print(f"Valores dos dados: {dado1}, {dado2}")
        print("-"*15)
    else:
        print("-"*15)
        print("Computador Ganhou!!")
        print(f"Valores dos dados: {dado1}, {dado2}")
        print("-"*15)
        
    escolha = input("Quer jogar novamente? \nSim - S \nNão - N\n")
    print("Fim do jogo")