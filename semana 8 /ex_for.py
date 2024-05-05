"""
1. Pares menores que 20, iniciando em zero
2. Pares entre 40 e 20, incluindo-os
3. Ímpares entre 10 e 30
4. Múltiplos de 4 entre 1 e 25
5. Divisores de 30 entre 10 e 20
6. Ímpares menores que x (informado pelo usuário)
7. Múltiplos de 7 entre a e b (informado pelo usuário) """


# print("Pares menores que 20, iniciando em zero:")
# for i in range(0, 20, 2):
#     print(i)

# print("Pares entre 40 e 20, incluindo-os:")
# for i in range(40, 20-1, -1):
#     print(i)

# print("Ímpares entre 10 e 30:")
# for i in range(10, 30):
#     if i % 2 == 1:
#         print(i)

# print("Múltiplos de 4 entre 1 e 25.")
# for i in range(1, 25):
#     if i % 4 == 0:
#         print(i)

# print("Divisores de 30 entre 10 e 20:")
# for i in range(10, 20):
#     if 30 % i == 0:
#         print(i)

# print("Ímpares menores que x (informado pelo usuário)")
# x = int(input("Informe um valor inteiro: "))
# for i in range(x):
#     if i % 2 == 1:
#         print(i)

# print("Múltiplos de 7 entre a e b (informado pelo usuário)")
# a = int(input("Informe um valor inteiro: "))
# b = int(input("Informe um valor inteiro: "))

# for i in range(a, b+1):
#     if i % 7 == 0:
#         print(i)

# para todo número de 1 a 100 que seja multiplo de 4 ou termine em 4, substitua por PIM

for i in range(1, 100):
    if (i % 4 == 0) or (i % 10 == 4):
        i = "PIM"
    print(i)