a, b, c = map(int, input() .split())
maior = ((a+b)+abs(a-b))/2
if c > maior:
    maior = c
print(f'{maior} eh o maior')
