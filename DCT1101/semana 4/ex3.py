ano = int(input("Informe um ano: "))

if (ano%4 == 0) and (ano%100 != 0) or (ano%400 == 0): # não usa & nem |
    print("O ano informado é bissexto")
else:
    print("O ano informado não é bissexto")
    