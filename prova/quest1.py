ano = int(input("ano: "))
a = ano % 19
b = ano % 4
c = ano % 7
d = (a * 19 + 24) % 30
e = (b * 2 + c * 4 + d * 6 + 5) % 7
# f = d + e + 22
f = 43

if f <= 31:
    print("A pascoa sera no dia: %02d/abr/%04d"%(f,ano)) # %02: duas casas, casa vazia fica 0
else:
    f = f - 31
    print("A pascoa sera no dia: %02d/abr/%04d"%(f,ano))
    