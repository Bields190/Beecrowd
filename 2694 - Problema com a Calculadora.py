qtd = int(input())
for i in range(qtd):
    soma = 0
    linha = input()
    #X X 0 0 X 0 0 0 X X X 0 0
    #0 1 2 3 4 5 6 7 8 9 0 1 2
    a = int(linha[2:4])
    b = int(linha[5:8])
    c = int(linha[11:13])
    soma = a + b + c
    print(soma)
