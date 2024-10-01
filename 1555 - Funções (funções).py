def funcoes(x, y):
    rafael = ((3*x)*(3*x))+y*y
    beto = 2*(x*x)+((5*y)*(5*y))
    carlos = -100*x+(y*y*y)
    if rafael > beto and rafael > carlos:
        maior = "Rafael"
    elif beto > rafael and beto > carlos:
        maior = "Beto"
    else:
        maior = "Carlos"

    return maior

qtd = int(input())
for i in range(qtd):
    x, y = map(int, input().split())
    print(funcoes(x, y), "ganhou")