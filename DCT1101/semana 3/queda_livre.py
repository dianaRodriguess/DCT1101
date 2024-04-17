# formula para descobrir o tempo = t² = (2.h) / g

from math import ceil, sqrt


altura = float(input("Qual a altura da queda? "))

gravidade = 9.81

calculo_tempo = (2 * altura) / gravidade

raiz = sqrt(calculo_tempo)

print(f"Vai levar {raiz:.1f}s para esse objeto cair.")
