""" from datetime import datetime

def calcular_idade(data_nascimento):
    data_atual = datetime.now()
    diferenca = data_atual - data_nascimento

    anos = diferenca.days // 365
    meses = (diferenca.days % 365) // 30
    dias = (diferenca.days % 365) % 30

    return anos, meses, dias

def main():
    data_nascimento_str = input("Digite sua data de nascimento (no formato DD/MM/AAAA): ")
    data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")

    anos, meses, dias = calcular_idade(data_nascimento)

    print(f"Você tem {anos} anos, {meses} meses e {dias} dias.")

if __name__ == "__main__":
    main() """

import calendar
import datetime

data = datetime.date.today()

ano_atual = data.year
mes_atual = data.month
dia_atual = data.day

ano_nasc = int(input("Informe seu ano de nascimento: "))
mes_nasc = int(input("Informe seu mês de nascimento (em número): "))
dia_nasc = int(input("Informe seu dia de nascimento (em número): "))

# Tratamento para meses e anos bissextos
if mes_atual == 1:
    ano_atual -= 1
    mes_atual = 12
else:
    mes_atual -= 1

num_dias = calendar.monthrange(ano_atual, mes_atual)[1]

anos = ano_atual - ano_nasc

if mes_atual > mes_nasc or (mes_atual == mes_nasc and dia_atual >= dia_nasc):
    meses = mes_atual - mes_nasc
    dias = dia_atual - dia_nasc if dia_atual >= dia_nasc else dia_atual + (num_dias - dia_nasc)
else:
    anos -= 1
    meses = 12 - (mes_nasc - mes_atual)
    dias = dia_atual - dia_nasc if dia_atual >= dia_nasc else dia_atual + (num_dias - dia_nasc)

print(f"Você tem {anos} anos, {meses} meses e {dias} dias.")

