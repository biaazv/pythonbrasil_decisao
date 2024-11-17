#variavel qtd_notas usada em caso de manutenção no código, variável média usada para melhor legibilidade
notas = 0.0
qtd_notas = 0

while(qtd_notas < 2):
    nota = float(input("Digite a nota: "))
    notas += nota
    qtd_notas += 1

media = notas/qtd_notas

if (media == 10.0):
    print("Aprovado com distinção")
elif (media >= 7.0):
    print("Aprovado")
else:
    print("Reprovado")

 