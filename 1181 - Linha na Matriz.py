M = []
l = int(input())
T = input()
# LEITURA::::::::::
for i in range(12):
    linha = []
    for j in range(12):
        var = float(input())
        linha.append(var)
    M.append(linha)
if T == 'S':
    soma = sum(M[l])
    print(f'{soma:.1f}')
elif T == 'M':
    soma = (sum(M[l])) / 12
    print(f'{soma:.1f}')
