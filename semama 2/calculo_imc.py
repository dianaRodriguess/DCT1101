altura_cm = int(input("Insira sua altura em centímetros: "))  # cm
peso = float(input("Insira seu peso em quilos: "))  # kg

altura_m = altura_cm/100

peso_ideal_H = (altura_cm - 100) - ((altura_cm - 150) / 4)
peso_ideal_M = (altura_cm - 100) - ((altura_cm - 150) / 2)

print()
print(f"Seu peso ideal é: {peso_ideal_H}kg")
print(f"Seu peso ideal é: {peso_ideal_M}kg")
print()

imc = peso / (altura_m **2)
print(f"Seu IMC: {imc:.2f}")
print()

def classificar_risco(imc):
    if imc <= 18.5:
        return "Abaixo do peso"
    elif 18.6 <= imc <= 24.9:
        return "Saudável"
    elif 25.0 <= imc <= 29.9:
        return "Sobrepeso"
    elif 30.0 <= imc <= 34.9:
        return "Obesidade Grau I (leve)"
    elif 35.0 <= imc <= 39.9:
        return "Obesidade Grau II (severa)"
    else:
        return "Obesidade Grau III (mórbida)"

risco = classificar_risco(imc)

print("| IMC              | Risco                           |")
print("|------------------|---------------------------------|")
print("| ≤ 18,5           | Abaixo do peso                  |")
print("| 18,6 - 24,9      | Saudável                        |")
print("| 25,0 - 29,9      | Sobrepeso                       |")
print("| 30,0 - 34,9      | Obesidade Grau I (leve)         |")
print("| 35,0 - 39,9      | Obesidade Grau II (severa)      |")
print("| ≥ 40,0           | Obesidade Grau III (mórbida)    |")

print()
print(f"Sua classificação de risco é: {risco}")

