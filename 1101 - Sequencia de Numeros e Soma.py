m = ""
n = ""
while m != 0 or n != 0:
    m, n = map(int, input().split())
    if m > n:
        m, n = n, m
    soma = 0
    if m <= 0 or n <= 0:
        exit()
    else:
        for i in range(m, n+1):
            soma += i
            print(i, end=' ')
        print(f"Sum={soma}")
