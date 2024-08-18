while True:
    Mat = []
    tam = int(input())
    if tam == 0:
        break
    else:
        for i in range(tam):
            aux = []
            for j in range(tam):
                if i > j:
                    aux.append(i-j+1)
                else:
                    aux.append((j-i)+1)
            Mat.append(aux)
        for i in range(tam):
            for j in range(tam):
                if j == tam-1:
                    print(f'{Mat[i][j]:3}', end="")
                else:
                    print(f'{Mat[i][j]:3}', end=" ")
            print()
        print()
