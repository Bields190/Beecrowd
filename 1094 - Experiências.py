qtd = int(input())
quan = ""
coel = 0
tot_coel = 0
sapo = 0
tot_sapo = 0
rat = 0
tot_rat = 0
tot = 0
for i in range(0, qtd):
    quan, tipo = map(str, input().split())
    quan = int(quan)
    if tipo == "C":
        tot_coel += quan
        tot += quan
    elif tipo == "S":
        tot_sapo += quan
        tot += quan
    elif tipo == "R":
        tot_rat += quan
        tot += quan
print(f"Total: {tot} cobaias")
print(f"Total de coelhos: {tot_coel}")
print(f"Total de ratos: {tot_rat}")
print(f"Total de sapos: {tot_sapo}")
print(f"Percentual de coelhos: {(tot_coel*100)/tot:.2f} %")
print(f"Percentual de ratos: {(tot_rat*100)/tot:.2f} %")
print(f"Percentual de sapos: {(tot_sapo*100)/tot:.2f} %")