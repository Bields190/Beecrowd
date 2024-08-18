l, c = map(int, input().split())
Mat = []
lin = []
for i in range(l):
    linha = list(map(int, input().split()))
    Mat.append(linha)
maior = 0
auxc = 0
auxl = 0
for i in range(l):
    auxc = 0
    elinha = sum(Mat[i])
    if elinha > maior:
        maior = elinha

for j in range(c):
    auxc = 0
    for i in range(l):
        auxc += Mat[i][j]
    if auxc > maior:
        maior = auxc
print(maior)