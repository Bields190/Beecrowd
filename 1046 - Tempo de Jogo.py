a, b = map(int, input().split())
if b>a:
    dur = a-b
    if dur<0:
        dur = dur*(-1)
else:
    temp = a-b
    if temp<0:
        temp = temp * (-1)
    dur = 24-temp
print(f'O JOGO DUROU {dur} HORA(S)')