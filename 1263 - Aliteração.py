while True:
    try:
        frase = (input().lower().split())
        ali = 0
        for i in range(1, len(frase)):
            quant = 0
            pal1 = frase[i-1][0]
            pal2 = frase[i][0]
            if pal1 == pal2:
                quant += 1
            else:
                break
            if quant >= 1:
                ali += 1
        print(ali)
    except EOFError:
        break
#######################DEPOIS FAÇO