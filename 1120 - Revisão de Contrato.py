while True:
    qtd, contrato = map(str, input().split())
    if qtd == "0" and contrato == "0":
        break
    else:
        lista = list(contrato)
        for i in range(lista.count(qtd)):
            lista.remove(qtd)
        if len(lista) == 0:
            print("0")
        else:
            string = "".join(lista)
            inteiro = int(string)
            print(inteiro)
