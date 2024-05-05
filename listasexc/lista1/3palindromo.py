'''Um número é dito palíndromo se tanto quando lido de frente para trás quanto de trás para
frente, representam a mesma quantidade. Por exemplo, 55, 131 e 12821 são números
palíndromos. Quantos palíndromos há com dois dígitos, ou seja, entre 10 e 99? Quantos
palíndromos há com três dígitos? Você é capaz de dizer quantos palíndromos existem com
quatro e com cinco dígitos?'''

print("Verifique quantos palídromos existem entre dois números")
print()
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

pal = 0

for i in range(n1,n2+1):
    i = str(i)
    iv = i[::-1]
  
    if iv == i:
        #print(f"{i} é um palídromo")
        pal += 1

print(f"Existem {pal} palíndromos entre esses números.")
