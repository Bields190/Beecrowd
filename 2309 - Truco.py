cartas = [4, 5, 6, 7, 12, 11, 13, 1, 2, 3]
qtd = int(input())
ad = 0; ber = 0
for i in range(qtd):
    a = 0; b = 0
    partida = list(map(int, input().split()))
    for j in range(3):
        if cartas.index(partida[j]) >= cartas.index(partida[j-3]):
            a += 1
        else:
            b += 1
    if a>b:
        ad += 1
    else:
        ber += 1
print(ad, ber, sep=" ")
