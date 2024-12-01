import math
a = float(input("Digite o valor de a: "))

if a == 0:
    print("A equação não possui raizes reais.")
    exit()
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    
delta = (b ** 2) - (4 * a * c)

if delta < 0:
    print("A equação não possui raizes reais.")
else:
    x1 = (-b + math.sqrt(delta)) / 2 * a
    x2 = (-b - math.sqrt(delta)) / 2 * a

    if delta == 0:
        print(f"1 Raiz: {x1}")
    else: 
        print(f"2 Raízes: {x1} e {x2}")