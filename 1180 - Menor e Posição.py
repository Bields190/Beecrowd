x = []
pos = 0
n = int(input())
x = list(map(int, input().split()))
menor = x[0]
for i in range(0, n):
    if x[i] < menor:
        menor = x[i]
        pos = i
print(f"Menor valor: {menor}\nPosicao: {pos}")