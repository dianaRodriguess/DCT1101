# velocidade distancia (km) / tempo (h)   | distancia (m)  /   tempo (s)
# 1h = 3600s
""" distancia = 24.7
tempo = (60 + 27) / 60

vel1 = distancia / tempo
vel2 = vel1 / 3.6

print(vel1, vel2) """


distancia = float(input("Qual a distância percorrida? "))
tempo_horas = float(input("Qual o tempo em horas? "))
tempo_min = float(input("E os minutos? "))
    
tempo = ((tempo_horas*60) + tempo_min) / 60

distancia_metro = distancia * 1000
tempo_sec = tempo * 3600

velocidade_media = distancia / tempo
velocidade_sec = distancia_metro / tempo_sec
# print(tempo)
print(f"Sua velociade média em km/h é: {velocidade_media:.2f}")
print(f"Sua velociade média em m/s é: {velocidade_sec:.2f}")
