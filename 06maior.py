qtd_num = 0
num_maior = 0
while (qtd_num < 3):
    num = float(input("Digite um número: "))
    if (num > num_maior):
        num_maior = num
    qtd_num += 1
print(f"O número maior é: {num_maior}")