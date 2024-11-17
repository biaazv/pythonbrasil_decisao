qtd_numeros = 0
lista_numeros = []

while(qtd_numeros < 3):
    numero = float(input("Digite um número: "))
    lista_numeros.append(numero)
    qtd_numeros +=1

print(f"Lista em ordem decrescente: {sorted(lista_numeros, reverse=True)}")