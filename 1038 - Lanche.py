total = 0.0
a, b = map(int, input().split())
#A
if a == 1:
    total += 4.00
elif a == 2:
    total += 4.50
elif a == 3:
    total += 5.00
elif a == 4:
    total += 2.00
elif a == 5:
    total += 1.50
valor = total * b
print(f'Total: R$ %.2f'%valor)