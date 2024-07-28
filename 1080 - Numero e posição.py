var = 0
pos = 0
for i in range(1, 101):
    num = int(input())
    if num > var:
        var = num
        pos = i
print(var)
print(pos)