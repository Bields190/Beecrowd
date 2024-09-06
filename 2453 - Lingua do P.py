pezado = input()
lista = pezado.split()
coiso = []
for i in range(len(lista)):
    boa = []
    for j in range(1, len(lista[i]), 2):
        boa.append(lista[i][j])
    coiso.append(boa)
for i in range(len(coiso)):
    for j in range(len(coiso[i])):
        print(coiso[i][j], end='')
    if i != len(coiso)-1:
        print(" ", end="")
    else:
        print("")