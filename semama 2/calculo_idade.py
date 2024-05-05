
import datetime


nome = input("Qual seu nome? ")
ano_nas = input("Qual o ano que você nasceu? ")

data = datetime.date.today()
ano = data.year

idade = ano - int(ano_nas)

print(f"Seu nome é {nome} e sua dade é {idade}.")

if idade < 18:
    print("Você é menor de idade. Não pode beber. :(")
elif idade >= 18:
    print("Você é maior de idade. Já pode beber. :)")
else:
    print("Error!")