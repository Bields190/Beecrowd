salario = float(input())
imposto = 0

if salario <= 2000.00:
    print("Isento")
else:
    if salario > 2000.00 and salario <= 3000.00:
        imposto += (salario - 2000.00) * 0.08
    elif salario > 3000.00 and salario <= 4500.00:
        imposto += (1000.00) * 0.08
        imposto += (salario - 3000.00) * 0.18
    elif salario > 4500.00:
        imposto += (1000.00) * 0.08
        imposto += (1500.00) * 0.18
        imposto += (salario - 4500.00) * 0.28
    print(f"R$ {imposto:.2f}")