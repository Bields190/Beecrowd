nome1, dia1 = input().split()
dia1 = int(dia1)
h1, m1, s1 = map(int, input().split(":"))
nome2, dia2 = input().split()
dia2 = int(dia2)
h2, m2, s2 = map(int, input().split(":"))

total_seconds1 = dia1 * 86400 + h1 * 3600 + m1 * 60 + s1
total_seconds2 = dia2 * 86400 + h2 * 3600 + m2 * 60 + s2

total_diff_seconds = total_seconds2 - total_seconds1

dias = total_diff_seconds // 86400
total_diff_seconds %= 86400
horas = total_diff_seconds // 3600
total_diff_seconds %= 3600
minutos = total_diff_seconds // 60
segundos = total_diff_seconds % 60

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")
