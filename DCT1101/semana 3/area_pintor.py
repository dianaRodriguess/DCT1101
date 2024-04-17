#           pintor

comprimento = float(input("Qual o comprimento? "))
largura = float(input("Qual a largura? "))
altura = float(input("Qual a altura? "))

area1 = largura * comprimento
area2 = largura * altura
area3 = altura * comprimento

area_total = area1 + (2 * area2) + (2 * area3)

print(f"A área toral a ser pintada é {area_total}m²")
