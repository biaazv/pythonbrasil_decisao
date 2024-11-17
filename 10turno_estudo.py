#executar a partir do python 3.10
turno = input("Turno de estudo M- matutino, v - vespertino ou n - noturno: ").lower()

match turno:
    case 'm':
        print("Bom dia!")
    case 'v':
        print("Bom tarde!")
    case 'n':
        print("Bom noite!")
    case _:
        print("Valor inválido!")
