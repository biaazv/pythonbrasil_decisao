salario_atual = float(input("Digite seu salário: "))
reajuste = 0
if (salario_atual <= 280.0):
    reajuste = 0.2
elif (280 < salario_atual < 700):
    reajuste = 0.15
elif (700 <= salario_atual < 1500):
    reajuste = 0.10
else:
    reajuste = 0.05

valor_aumento = reajuste * salario_atual

print(f"Salário atual {salario_atual}")
print(f"Percentual de aumento: {reajuste}")
print(f"Valor do aumento: {valor_aumento}")
print(f"Novo salário: {salario_atual + valor_aumento}")