b = int(input())
for i in range(b):
    a = int(input())
    num = 0
    for i in range(1,a):
        if (a%i == 0):
            num = (num+i)
    if (num == a):
        print(f'{a} eh perfeito')
    else:
        print(f'{a} nao eh perfeito')