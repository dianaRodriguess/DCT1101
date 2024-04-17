
bolo = 0
sorvete = 0
mousse = 0

total = int(input("Quantas pessoa vão ser entrevistadas? "))

texto_escolhas = """
Estamos fazendo uma pesquisa sobre a melhor sobremesa. 
Essas são as opções: Bolo, Sorvete e Mousse.

Para votar digite: 
1 - BOLO
2 - SORVETE
3 - MOUSSE
"""
print(texto_escolhas)

for i in range(total):
    voto = int(input(f"{i+1}° a votar. Em quem você vota: "))
    
    match voto:
        case 1: 
            bolo += 1
        case 2:
            sorvete += 1
        case 3:
            mousse += 1
        case _:
            print("Valor incorreto.")
            
texto_reslt = f"""
Votações encerradas.

Bolo recebeu {bolo} votos
Sorvete recebeu {sorvete} votos
Mousse recebeu {mousse} votos
"""

print(texto_reslt)




