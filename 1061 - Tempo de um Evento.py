nome1, dia1 = map(str, input().split())
dia1 = int(dia1)
h1, m1, s1 = map(int, input().split(":"))
nome2, dia2 = input().split()
dia2 = int(dia2)
h2, m2, s2 = map(int, input().split(":"))

tot_sec1 = dia1 * 86400 + h1 * 3600 + m1 * 60 + s1
tot_sec2 = dia2 * 86400 + h2 * 3600 + m2 * 60 + s2

tottot_sec = tot_sec2 - tot_sec1

dias = tottot_sec // 86400
tottot_sec %= 86400
horas = tottot_sec // 3600
tottot_sec %= 3600
minutos = tottot_sec // 60
segundos = tottot_sec % 60

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")
