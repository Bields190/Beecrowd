sn = 0
while sn != 2:
    qtd = 0
    soma = 0
    while qtd !=2:
        nota = float(input())
        if nota < 0 or nota > 10:
            print("nota invalida")
        else:
            qtd += 1
            soma += nota
    print(f'media = {soma / qtd:.2f}')
    while sn != 1 or sn != 2:
        sn = int(input('novo calculo (1-sim 2-nao)\n'))
        if sn == 2:
            quit()
        elif sn == 1:
            break
