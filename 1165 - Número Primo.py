qtd = int(input())
for i in range(qtd):
    ver = 0
    n = int(input())
    for j in range(1,n+1):
        if n%j == 0:
            ver += 1
    if ver == 2:
        print(f"{n} eh primo")
    else:
        print(f"{n} nao eh primo")