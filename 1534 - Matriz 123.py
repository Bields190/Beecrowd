while True:
    try:
        qtd = int(input())
        mat = []
        for i in range(qtd):
            linha = []
            for j in range(qtd):
                if (i+j) == qtd-1:
                    linha.append(2)
                elif i == j:
                    linha.append(1)
                else:
                    linha.append(3)
            mat.append(linha)
        for i in range(qtd):
            for j in range(qtd):
                print (mat[i][j], end="")
            print()
    except(EOFError):
        break
