val = float(input())
cem = 0
cinq = 0
vint = 0
dez = 0
cinc = 0
dois = 0
um = 0
cinqcen = 0
vincent = 0
dezcent = 0
cinccent = 0
umcent = 0

#NOTAS:
while round(val, 2) >= 100.00:
    val -= 100.00
    cem += 1
while round(val, 2) >= 50.00:
    val -= 50.00
    cinq += 1
while round(val, 2) >= 20.00:
    val -= 20.00
    vint += 1
while round(val, 2) >= 10.00:
    val -= 10.00
    dez += 1
while round(val, 2) >= 5.00:
    val -= 5.00
    cinc += 1
while round(val, 2) >= 2.00:
    val -= 2.00
    dois += 1
#MOEDAS:
while round(val, 2) >= 1.00:
    val -= 1.00
    um += 1
while round(val, 2) >= 0.50:
    val -= 0.50
    cinqcen += 1
while round(val, 2) >= 0.25:
    val -= 0.25
    vincent += 1
while round(val, 2) >= 0.10:
    val -= 0.10
    dezcent += 1
while round(val, 2) >= 0.05:
    val -= 0.05
    cinccent += 1
while round(val, 2) >= 0.01:
    val -= 0.01
    umcent += 1

print("NOTAS:")
print(f'{cem} nota(s) de R$ 100.00')
print(f'{cinq} nota(s) de R$ 50.00')
print(f'{vint} nota(s) de R$ 20.00')
print(f'{dez} nota(s) de R$ 10.00')
print(f'{cinc} nota(s) de R$ 5.00')
print(f'{dois} nota(s) de R$ 2.00')
print("MOEDAS:")
print(f'{um} moeda(s) de R$ 1.00')
print(f'{cinqcen} moeda(s) de R$ 0.50')
print(f'{vincent} moeda(s) de R$ 0.25')
print(f'{dezcent} moeda(s) de R$ 0.10')
print(f'{cinccent} moeda(s) de R$ 0.05')
print(f'{umcent} moeda(s) de R$ 0.01')