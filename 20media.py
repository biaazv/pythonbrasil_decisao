'''
20. Faça um Programa para leitura de três notas parciais de um aluno.
O programa deve calcular a média
alcançada por aluno e presentar:
a. A mensagem "Aprovado", se a média for maior ou igual a 7, com a
respectiva média alcançada;
b. A mensagem "Reprovado", se a média for menor do que 7, com a r
'''
media = 0
qtd_notas = 3

for i in range(qtd_notas):
    nota = float(input("Digite a nota: "))
    media += nota
media = media/qtd_notas

if(media>=7):
    print(f"Aprovado, média {media}")
else:
    print(f"Reprovado, média {media}")