val = int(input())
print(val)
cem = 0
cinq = 0
vint = 0
dez = 0
cinc = 0
dois = 0
um = 0
while val>=100:
    val = val-100
    cem = cem+1
while val>=50:
    val = val-50
    cinq = cinq+1
while val>=20:
    val = val-20
    vint = vint+1
while val>=10:
    val = val-10
    dez = dez+1
while val>=5:
    val = val-5
    cinc = cinc+1
while val>=2:
    val = val-2
    dois = dois+1
while val>=1:
    val = val-1
    um = um+1
print(f'{cem} nota(s) de R$ 100,00')
print(f'{cinq} nota(s) de R$ 50,00')
print(f'{vint} nota(s) de R$ 20,00')
print(f'{dez} nota(s) de R$ 10,00')
print(f'{cinc} nota(s) de R$ 5,00')
print(f'{dois} nota(s) de R$ 2,00')
print(f'{um} nota(s) de R$ 1,00')