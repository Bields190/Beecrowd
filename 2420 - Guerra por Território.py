a = []; soma = 0; somar = 0
qtd = int(input())
a = list(map(int, input().split()))
for i in range(qtd):
    soma += a[i]
for i in range(qtd):
    somar += a[i]
    if somar == soma/2:
        ain = i+1
print(ain)
