sal = float(input())
if sal<=400.00:
    por = 15
    aum = ((sal*por)/100)
    novosal = sal + aum
elif sal>400.00 and sal<=800.00:
    por = 12
    aum = ((sal*por)/100)
    novosal = sal + aum
if sal>800.00 and sal<=1200.00:
    por = 10
    aum = ((sal*por)/100)
    novosal = sal + aum
elif sal>1200.00 and sal<=2000.00:
    por = 7
    aum = ((sal*por)/100)
    novosal = sal + aum
elif sal>2000.00:
    por = 4
    aum = ((sal*por)/100)
    novosal = sal + aum
print(f"Novo salario: %.2f"%novosal) 
print(f"Reajuste ganho: %.2f"%aum) 
print(f'Em percentual: {por} %')