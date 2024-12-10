'''
19. Faça um Programa que leia um número inteiro menor que 1000 e
imprima a quantidade de centenas, dezenas
e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros.
Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades
Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21,
11, 1, 7 e 16
'''
import math

numero = int(input("Digite um número até 1000: "))

centenas = math.floor(numero / 100)
dezenas = math.floor((numero - (centenas * 100)) / 10)
unidades = (numero - (centenas * 100) - (dezenas * 10))
resultado = ''

if (centenas > 0):
    resultado = resultado + str(centenas)
    if (centenas > 1):
        resultado = resultado + ' centenas'
    else:
        resultado = resultado + ' centena'

if (dezenas > 0):
    if (unidades == 0) and (centenas != 0):
        resultado = resultado + ' e '
    if (unidades != 0) and (centenas != 0):
        resultado = resultado + ', '
    resultado = resultado +  str(dezenas)
    if (dezenas > 1):
        resultado = resultado + ' dezenas '
    else:
        resultado = resultado + ' dezena '

if (unidades > 0):
    if (centenas != 0) or (dezenas != 0):
        resultado = resultado + ' e '
    resultado = resultado + str(unidades)
    if (unidades > 1):
        resultado = resultado + ' unidades '
    else:
        resultado = resultado + ' unidade '

print(resultado)





