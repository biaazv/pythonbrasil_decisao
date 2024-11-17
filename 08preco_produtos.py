qtd_produtos = 0
lista_preco = []

#entrada de 3 produtos
while (qtd_produtos < 3):
    preco_produtos = float(input("Digite o valor do produto: "))
    #coloca os preços na lista
    lista_preco.append(preco_produtos)
    qtd_produtos += 1

#ordena a lista pelo preço dos produtos
lista_preco_ordenada = sorted(lista_preco)

#index usado para saber a posição do preço mais barato na lista original, 
# +1 para exibir a qtd de produtos a partir do 1 em vez de 0
print(f"O produto mais barato é o {(lista_preco.index(lista_preco_ordenada[0]) + 1)}")


