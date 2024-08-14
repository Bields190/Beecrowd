lista = []
qtd = int(input())
lista = list(map(int, input().split()))
maior = 0
num = 0
for i in range(qtd):
    cont = lista.count(lista[i])
    if cont > maior:
        maior = cont
        num = lista[i]
    elif cont == maior and lista[i] > num:
        num = lista[i]
print(num)