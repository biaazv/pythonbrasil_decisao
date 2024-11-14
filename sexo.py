#!/usr/bin/env python
#lower() usado para transaformar a string em lowercase caso o usuário digite uppercase
letra = input("Digite o sexo: ").lower()

if (letra == 'f'):
    print(f"feminino")
elif (letra == 'm'):
    print(f"masculino")
else:
    print(f"Sexo inválido")