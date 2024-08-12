empate = 0
gremio = 0
inter = 0
intera = 0
gremioa = 0
grenal = 0
val = 1
while val != 2:
    inter, gremio = map(int, input().split())
    grenal +=1
    if inter == gremio:
        empate += 1
    if inter > gremio:
        intera += 1
    if inter < gremio:
        gremioa += 1
    val = input('Novo grenal (1-sim 2-nao)\n')
    if val == '2':
        break
print(f"{grenal} grenais")
print(f'Inter:{intera}')
print(f'Gremio:{gremioa}')
print(f"Empates:{empate}")
if intera > gremioa:
    print("Inter venceu mais")
else:
    print("Gremio venceu mais")
