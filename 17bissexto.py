ano = int(input("Digite o ano: "))

2024/4
if (ano % 4 == 0):
    print("É divisível por 4")
    if (ano % 100 != 0):
        print("É ano bissexto")
    else:
        print("Não é ano bissexto")
else:
    print("Não é ano bissexto")