import random

num_sort = random.randint(1,100)

tentativa = 1
palpites = 0
while tentativa <= 10:
    num_escl = int(input("Adivinhe o número: "))
    palpites += 1
    if tentativa == 1:
        if (num_escl == num_sort):
            print("Você teve muita sorte!!")
            break
        elif (num_escl > num_sort):
            print("Digite um número menor.")
        else:
            print("Digite um número maior.")
    elif tentativa == 2:
        if (num_escl == num_sort):
            print("Você joga bem, mas ainda contou com a sorte!!")
            break
        elif (num_escl > num_sort):
            print("Digite um número menor.")
        else:
            print("Digite um número maior.")
    else:
        if (num_escl == num_sort):
            print("Você é um exelente estrategista")
            break
        else:
            print("Analise melhor sua estratégia antes de jogar novamete.")
            
    # num_escl = int(input("Adivinhe o número: "))
    tentativa += 1
    if tentativa > 10:
        e = input("Quer jogar novamente? S/N: ")
        if e.lower() == 's':
            tentativa = 1

print()
print(f"Número aleatório: {num_sort}\n"+
      f"Número escolhido: {num_escl}")
print(f"Palpites: {palpites}")
