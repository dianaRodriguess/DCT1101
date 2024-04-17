x = 1
y = 2
z = 3

resp_a = x >= y
print(f"Letra a: {resp_a}")

resp_b = x <= y and y < z
print(f"Letra a: {resp_b}")

resp_c = not (x >= y)
print(f"Letra c: {resp_c}")

resp_d = x >= (z - 2)
print(f"Letra d: {resp_d}")

resp_e = (x > z) and (x < y)
print(f"Letra e: {resp_e}")