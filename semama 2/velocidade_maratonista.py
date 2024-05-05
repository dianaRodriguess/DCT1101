# performance min / Km

distancia = float(input("Digite a distância em quilômetros: "))# Km
tempo_horas = float(input("Digite o tempo em horas: "))  # min
tempo_min = float(input("Agora os minutos: "))

tempo = ((tempo_horas * 60) + tempo_min) / 60

t_min = tempo * 60
ritimo1 = t_min / distancia

t_sec = int((ritimo1 - int(ritimo1)) * 60)
# ritimo2 = int(ritimo1)
tempo_sec = f"{int(ritimo1)}.{t_sec}"

print()
print(f"Sua performance foi: {ritimo1:.4f} min/km")
print(f"Sua performance foi: {tempo_sec} sec/km")

