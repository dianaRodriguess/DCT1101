import random


""" jogador = int(input("Escolha de acordo: 1-Pedra; 2-Papel; 3-Tesoura: "))



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

if jogador == ppt.values():
    print(ppt.values())
    
for key, value in ppt.items():
    if jogador == value:
        print("Jogador: ", key)
    if id == value:
        print("Computador: ", key)
    

# print(f"computador {id}, jogador {jogador}") """

i = 1 
while i <= 3:
    print(i)
    i += 1