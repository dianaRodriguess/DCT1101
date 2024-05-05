import random

mesadas_possiveis = [" R$ 20,00", " R$ 40,00", " R$ 60,00", " R$ 80,00", "R$ 100,00"]

mesada1 = random.choice(mesadas_possiveis)
mesada2 = random.choice(mesadas_possiveis)
mesada3 = random.choice(mesadas_possiveis)

print("#" * 34)
print("#" * 3, "     SORTEIO MESADA       ", "#" * 3)
print("#" * 34)
print("#" * 3, f"   HUGUINHO: {mesada1}    ","#" * 3)
print("#" * 3, f"   ZEZINHO: {mesada2}     ","#" * 3)
print("#" * 3, f"   LUIZINHO: {mesada3}    ","#" * 3)
print("#" * 34)
