#!/usr/bin/env python
#considerando que o usuário digitará apenas letras 
letra = input("Digite uma letra: ")
vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z']
tipo = ''

if (isinstance(letra, str)):
    for i in vogais:
        if (letra == i):
            tipo = 'vogal'
    for j in consoantes:
        if (letra == j):
            tipo = 'consoante'
    print(f"{letra} é {tipo}")

