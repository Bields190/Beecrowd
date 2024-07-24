pos = 0
soma = 0
for i in range (0, 6):
    var = float(input())
    if var > 0:
        pos = pos+1
        soma += var
media = soma/pos
print(f"{pos} valores positivos")
print (f'%.1f'%media)