while True:
    try:
        val = True
        texto = str(input())
        lista = list(texto)
        for i in range(0, len(texto)):
            if lista[i] .isalpha() and val is True:
                lista[i] = lista[i].upper()
                val = False
            elif lista[i] .isalpha() and val is False:
                lista[i] = lista[i].lower()
                val = True
            else:
                continue
        string = "".join(lista)
        print(string)
    except EOFError:
        break
