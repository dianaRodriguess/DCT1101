
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
    voto = int(input(f"{i+1}° pessoa a votar. Em quem você vota: "))
    
    match voto:
        case 1: 
            bolo += 1
        case 2:
            sorvete += 1
        case 3:
            mousse += 1
        case _:
            print("Valor incorreto. Vote novamente")
            i = i - 1
            voto = int(input(f"{i+2}° pessoa a votar. Em quem você vota: "))
            # match voto:
            #     case 1: 
            #         bolo += 1
            #     case 2:
            #         sorvete += 1
            #     case 3:
            #         mousse += 1
            
perctB = bolo / total * 100
perctS = sorvete / total * 100
perctM = mousse / total * 100

texto_reslt = f"""
Votações encerradas.

Foram entrevistadas {total} pessooas.

Bolo recebeu {bolo} votos, totalizanado {perctB:.1f}% dos votos.
Sorvete recebeu {sorvete} votos, totalizando {perctS:.1f}% dos votos.
Mousse recebeu {mousse} votos, totalizando {perctM:.1f}% dos votos.
"""

print(texto_reslt)
