# pedir cada lado da fazenda
comprimento = float(input("Qual o comprimento? "))
largura = float(input("Qual a largura? "))

area =  comprimento * largura
perimetro = 2 * (comprimento + largura)

qtd_arame = 5 * perimetro

texto = f'''
A área da sua fazenda é {area}m².
O perimetro da sua fazenda é {perimetro} metros.
Precisa-se de {qtd_arame} metros de arame para cercar a fazenda.
'''

print(texto)