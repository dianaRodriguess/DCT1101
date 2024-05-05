'''Em tempos de corpolatria, o culto exagerado à beleza física e aos corpos esculturais, surgem
muitos medicamentos e dietas milagrosas que prometem perda de peso rapidamente. A
empresa Magri & Cela lançou o produto Chá Arlatão, um chá "milagroso" que promete ao
paciente emagrecer 7kg na primeira semana e, nas semana seguintes, o paciente perde
70% do peso que perdeu na semana anterior. Simule a perda de peso de um paciente de
100Kg, semana a semana, até que ele tenha perdido 20Kg'''

peso_inicial = 100
perda1 = 7
perda2 = 0.7*perda1
peso_final = peso_inicial - perda1

peso_meta = peso_inicial - 20

for i in range(5):
    peso_inicial = peso_final
    # perda2 = 0.7*perda1
    peso_final = peso_inicial - perda2
    perda2 = 0.7*perda2

print(peso_final)    

# while peso_final > peso_meta:
#     perda = 0.7*(peso_inicial - peso_final)
#     peso_final = peso_final - perda
#     peso_inicial = peso_final

#     if peso_final <= peso_meta:
#         print("você perdeu 20kg.")
#     else:
#         print("ainda falta")
#         perda = 0.7*(peso_inicial - peso_final)
#         peso_final = peso_inicial - perda
#         # peso_inicial = peso_final


