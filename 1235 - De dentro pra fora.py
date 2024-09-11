qtd = int(input())
for i in range(qtd):
    vey = []
    fudido = str(input())
    tam = int(len(fudido)/2)
    vey.append(fudido[tam-1::-1])
    vey.append(fudido[:tam-1:-1])
    mano = "".join(vey)
    print(mano)