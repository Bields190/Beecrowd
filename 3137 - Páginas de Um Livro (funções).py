def paginas(num):
    soma = 0
    for i in range(1, num+1):
        pag = str(i)
        soma += len(pag)

    return soma


quant = int(input())
print(paginas(quant))
