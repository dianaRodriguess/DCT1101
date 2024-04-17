celsius = float(input("Celcius: "))
fahrenheit = float(input("Fahrenheit: "))

temp_f = (9 / 5 * celsius) + 32
temp_c = (5 / 9) * (fahrenheit - 32)

print(f"Temperatura em Fahrenheit {temp_f} F°") # C para F
print(f"Temperatura em Celsius {temp_c} C°") # F para C
