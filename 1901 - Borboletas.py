tam = int(input())
Floresta = []
linha = []
bor = []
for i in range(tam):
    linha = list(map(int, input().split()))
    Floresta.append(linha)
for i in range(tam*2):
    lin, col = map(int, input().split())
    bor.append(Floresta[lin-1][col-1])
    contagem = bor.count(Floresta[lin-1][col-1])
    if contagem > 1:
        bor.remove(Floresta[lin-1][col-1])
print(len(bor))
