M = []
l = int(input())
T = input()
#LEITURA::::::::::
for i in range(12):
    linha = []
    for j in range(12):
        var = float(input())
        linha.append(var)
    M.append(linha)
soma = 0
if T == 'S':
    for i in range(12):
            soma += M[i][l]
    print(f'{soma:.1f}')
elif T == 'M':
    for i in range(12):
            soma += (M[i][l])/12
    print(f'{soma:.1f}')