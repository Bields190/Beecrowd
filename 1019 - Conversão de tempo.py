
temp = int(input())
hora = 0
minuto = 0
seg = 0
while temp>= 3600:
    temp = temp-3600
    hora = hora+1
while temp>=60:
    temp = temp-60
    minuto = minuto+1
while temp >=1:
    temp = temp-1
    seg = seg+1
print(f'{hora}:{minuto}:{seg}')