bandeijas = int(input())
soma = 0
for i in range(bandeijas):
    l, c = map(int, input().split())
    if l > c:
        soma += c
print(soma)
