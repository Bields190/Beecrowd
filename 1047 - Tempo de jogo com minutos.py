h1, m1, h2, m2 = map(int, input().split())

#hora
if h2 > h1 or (h2 == h1 and m2 > m1):
    dur = h2 - h1
else:
    dur = 24 - h1 + h2
#min
if m2 >= m1:
    min = m2 - m1
else:
    min = 60 - m1 + m2
    dur -= 1
if dur < 0:
    dur += 24

print(f'O JOGO DUROU {dur} HORA(S) E {min} MINUTO(S)')