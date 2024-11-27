qtd_horas = int(input("Digite a quantidade de horas trabalhadas: "))
vlr_hora  = float(input("Digite o valor da hora trabalhada: "))
ir = 0

salario_bruto = qtd_horas * vlr_hora

if (salario_bruto <= 900):
    ir = 0
elif (900 < salario_bruto <= 1500):
    ir = 0.05
elif (1550 < salario_bruto <= 2500):
    ir = 0.1

sindicato = salario_bruto * 0.03
fgts      = salario_bruto * 0.11
inss      = salario_bruto * 0.10
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos

print(f"Sálario bruto: ({vlr_hora} * {qtd_horas}) = R${salario_bruto}")
print(f"(-)IR: {salario_bruto * ir}")
print(f"(-)INSS: {salario_bruto * ir}")
print(f"(-)Sindicato: {sindicato}")
print(f"FGTS: {fgts}")
print(f"Total de descontos: R${descontos}")
print(f"Salário líquido: R${salario_liquido}")