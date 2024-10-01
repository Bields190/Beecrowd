def matematico(linha):
    result = 0
    if linha[1].isupper():
        result = int(linha[2])-int(linha[0])
    elif linha[1].islower():
        result = int(linha[2])+int(linha[0])
    if linha[0] == linha[2]:
        result = int(linha[0])*int(linha[2])

    return result


qtd = int(input())
for i in range(qtd):
    seq = input()
    print(matematico(seq))