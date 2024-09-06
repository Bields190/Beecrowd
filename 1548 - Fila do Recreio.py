casos = int(input())
for x in range(casos):
    qtd = int(input())
    M = list(map(int, input().split()))
    M2 = M.copy()
    M.sort(reverse=True)
    var = 0
    for item in range(qtd):
        if M[item] != M2[item]:
            var += 1
    print(qtd-var)
