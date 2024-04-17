import calendar
import datetime

data = datetime.date.today()

ano = data.year
mes = data.month
# mes = 2
dia = data.day
num_dias = calendar.monthrange(ano, mes-1)[1]  

ano_nasc = int(input("Informe seu ano de nascimento: "))
mes_nasc = int(input("Informe seu mês de nascimento (em número): "))
dia_nasc = int(input("Informe seu dia de nascimento (em número): "))

""" if mes > mes_nasc:
    print("Você já fez aniversário esse ano")
    
elif mes < mes_nasc:
    print("Você ainda vai fazer aniversário esse ano")
elif mes == mes_nasc:
    if dia == dia_nasc:
        print("Seu aniversário é hoje!!!")
    elif dia > dia_nasc:
        print("Seu aniversário já passou.")
    elif dia < dia_nasc:
        print("Seu aniversário ainda vai acontecer.")
    # print("print")
else: 
    print("error") """

anos = ano - ano_nasc

if mes > mes_nasc:
    if dia > dia_nasc:
        meses = mes - mes_nasc
        dias = dia - dia_nasc
        print(f"Você tem {anos} anos, {meses} meses e {dias} dias.")
    elif dia < dia_nasc:
        meses = mes - mes_nasc - 1
        dias = dia + (num_dias - dia_nasc)
        print(f"Você tem {anos} anos, {meses} meses e {dias} dias.")
    elif dia == dia_nasc:
        meses = mes - mes_nasc
        dias = 0
        print(f"Você tem {anos} anos, {meses} meses e {dias} dias.")
# tá errado, concerte
elif mes < mes_nasc:
    if dia > dia_nasc:
        meses = mes - mes_nasc
        dias = dia - dia_nasc
        print(f"Você tem {anos-1} anos, {meses} meses e {dias} dias.")
    elif dia < dia_nasc:
        meses = mes_nasc - mes
        dias = dia + (num_dias - dia_nasc)
        print(f"Você tem {anos-1} anos, {meses} meses e {dias} dias.")
    elif dia == dia_nasc:
        meses = mes - mes_nasc
        dias = 0
        print(f"Você tem {anos-1} anos, {meses} meses e {dias} dias.")
        