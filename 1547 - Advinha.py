qtd = int(input())
chutes = []
for i in range(qtd):
    qal, num = map(int, input().split())
    chutes = list(map(int, input().split()))
    val = chutes[0]
    ini = abs(chutes[0] - num)
    for j in range(qal):
        aux = abs(chutes[j] - num)
        if aux == 0:
            val = chutes[j]
            break
        elif aux < ini:
            ini = aux
            val = chutes[j]
    ind = chutes.index(val)
    print(ind + 1)
