qtd_num = 0
lista_numeros = []

while (qtd_num < 3):
    num = float(input("Digite um número: "))
    lista_numeros.append(num)
    qtd_num += 1
lista_ordenada = (sorted(lista_numeros))

print(f"O menor número é: {lista_ordenada[0]}")
print(f"O maior número é: {lista_ordenada[-1]}")

