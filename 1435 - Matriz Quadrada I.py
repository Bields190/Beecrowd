while True:
    mat = []
    tam = int(input())
    if tam == 0:
        break
    else:
        for i in range(tam):
            linha = []
            for j in range(tam):
                elemento = [i, j, tam-i-1, tam-j-1]
                elemento.sort()
                linha.append(f'{elemento[0] + 1:3}')
            mat.append(linha)
        for item in mat:
            print(*item)
        print()