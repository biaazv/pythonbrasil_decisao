'''
18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine
se a mesma é uma data válida.
'''
data = input("Digite uma data no formato: DD/MM/AAAA: ")
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])

# valida ano bissexto
bissexto = False
if (ano % 4 == 0):
    bissexto = True
    if (ano % 100 == 0) and (ano % 400 == 0):
        bissexto = False

valida = False
if (mes < 12):
    if (mes in (4, 6, 9, 11)):
        if dia <= 30:
            valida = True
    elif (mes in (1, 3, 5, 7, 8, 10, 12)):
        if dia <= 31:
            valida = True
    else: 
        if (bissexto):
            if dia <= 29:
                valida = True
        else:
            if dia <= 28:
                valida = True 
else:
    valida = False

if valida:
    print("Data válida")
else:
    print("Data inválida")



