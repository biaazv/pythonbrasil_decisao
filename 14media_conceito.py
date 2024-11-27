notas = []

while (len(notas) < 2):
    nota = float(input("Digite a nota: "))
    notas.append(nota)

media = (sum(notas))/2

if (9 < media <=10):
    conceito = 'A'
    aprovado = True
elif (7.5 < media < 9):
    conceito = 'B'
    aprovado = True
elif (6 < media < 7.5):
    conceito = 'C'
    aprovado = True
elif (4 < media < 6):
    conceito = 'D'
    aprovado = False
elif (0 < media < 4):
    conceito = 'E'
    aprovado = False
    



print(f"Notas: {notas[0]} e {notas[1]}")
print(f"Média: {media}")
print(f"Conceito: {conceito}")
if aprovado:
    print("Aprovado")
else:
    print("Reprovado")