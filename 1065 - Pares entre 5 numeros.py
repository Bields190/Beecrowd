pos = 0
soma = 0
for i in range (0, 5):
    var = int(input())
    if var%2==0:
        pos = pos+1
print(f"{pos} valores pares")