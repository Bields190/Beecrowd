num = int(input())
for i in range(num):
    comprou, precisa = map(int, input().split())
    coiso = comprou
    mais = 0
    if coiso >= precisa:
        while coiso >= precisa:
            coiso -= precisa
            mais += 1
        tot = coiso+mais
        print(tot)
    else:
        print(comprou)
