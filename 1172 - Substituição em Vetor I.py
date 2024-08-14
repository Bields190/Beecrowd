x = []
for i in range (0,10):
    num = int(input())
    if num <= 0:
        num = 1
    x.append(num)
for i in range (0,10):
    print(f"X[{i}] = {x[i]}")