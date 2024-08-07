n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if  y != 0:
        print(x/y)
    else:
        print("divisao impossivel")