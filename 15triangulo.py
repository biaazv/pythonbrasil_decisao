#!/usr/bin/env python
lados = []
valida_triangulo = False

while (len(lados) < 3):
    lado = int(input("Digite o lados do triangulo: "))
    lados.append(lado)

if ((lados[0] + lados[1]) < lados[2]) or ((lados[0] + lados[2]) < lados[1]) or ((lados[1] + lados[2]) < lados[0]):
        print("Não é triângulo")
else:
    if lados[0] == lados[1] == lados[2]:
        print("Triângulo Equilátero")
    elif (lados[0] == lados[1]) or (lados[0] == lados[2]) or (lados[1] == lados[2]):
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno") 
