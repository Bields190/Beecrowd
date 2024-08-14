a = 1
while True:
    n = []; c = []; big = []; maior = 0
    qtd = int(input())
    if qtd != 0:
        for i in range(qtd):
            cod, nota = map(int, input().split())
            c.append(cod); n.append(nota)
            if nota > maior:
                maior = nota
                big = [cod]
            elif nota == maior:
                big.append(cod)
        print(f"Turma {a}")
        for cod in big:
            print(cod, end=" ")
        print("\n")
        a += 1
    else:
        break
