x = int(input())
y = int(input())
soma = 0
#if y>x:
#    y,x=x,y
for i in range(x-1, y, -1):
    if i%2 == 1:
        soma += i
print(soma)