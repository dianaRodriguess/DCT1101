n1 = float(input("nota 1: "))
n2 = float(input("nota 2: "))
n3 = float(input("nota 3: "))

if (n1 <= n2) and (n2 <= n3):
    menor1 = n1
    menor2 = n2
    melhor = n3
    
    media1 = (((menor1 + menor2) / 2) + melhor) /2
    media2 = (n1 + n2 + n3)/3
    
    print(f"Media do professor: {media1:.1f}")
    print(f"Media do aritimetica: {media2:.1f}")
elif (n2 <= n3) and (n3 <= n1):
    menor1 = n2
    menor2 = n3
    melhor = n1
    
    media1 = (((menor1 + menor2) / 2) + melhor) /2
    media2 = (n1 + n2 + n3)/3
    
    print(f"Media do professor: {media1:.1f}")
    print(f"Media do aritimetica: {media2:.1f}")
else:
    menor1 = n1
    menor2 = n3
    melhor = n2
    
    media1 = (((menor1 + menor2) / 2) + melhor) /2
    media2 = (n1 + n2 + n3)/3
    
    print(f"Media do professor: {media1:.1f}")
    print(f"Media do aritimetica: {media2:.1f}")
