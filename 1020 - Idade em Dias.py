a = int(input())
ano = 0
mes = 0
dia = 0
while a >= 365:
    a = a-365
    ano = ano+1
while a >= 30:
    a = a-30
    mes = mes+1
print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{a} dia(s)')