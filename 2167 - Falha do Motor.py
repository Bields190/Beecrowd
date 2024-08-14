n = []
ind = 0
qtd = int(input())
n = list(map(int, input().split()))
for i in range(qtd-1):
    if n[i+1] < n[i]:
        ind = i+2
        break
print(ind)