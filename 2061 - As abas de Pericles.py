n, m = map(int, input().split())
for i in range(m):
    acao = input()
    if acao == 'fechou':
        n += 1
    else:
        n -= 1
print(n)
