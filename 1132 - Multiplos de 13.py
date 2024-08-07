a = int(input())
b = int(input())
soma = 0
for i in range(a,b+1):
    if i%13 == 0:
        continue
    soma += i
print(soma)