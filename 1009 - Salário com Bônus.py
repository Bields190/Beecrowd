nome = input()
sal = float(input())
vendas = float(input())
porc = 0.15*vendas
salario = porc + sal
print(f'TOTAL = R$ %.2f'%salario)