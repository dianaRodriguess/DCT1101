try:
    
    print("Usuário 1")
    nome1 = input("Digite seu nome: ")
    idade1 = int(input("Agora digite sua idade: "))

    print("Usuário 2")
    nome2 = input("Digite seu nome: ")
    idade2 = int(input("Agora digite sua idade: "))

    if idade1 > idade2:
        print(f"{nome1} é mais velho.")
    elif idade2 > idade1:
        print(f"{nome2} é mais velho.")
    else:
        print("Vocês tem a mesma idade.")

except ValueError:
    print("Esse valor não é válido.")
    
