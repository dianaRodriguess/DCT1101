from math import sqrt

a = float(input("lado a: "))
b = float(input("lado b: "))
c = float(input("lado c: "))

p = (a + b + c) / 2
s = p * (p - a) * (p - b) * (p - c)

if s > 0:
    area = sqrt(abs(s))
    print(f"area é: {area:.2f}")
else:
    print("Não forma trinângulo.")
    