#MINHASOLUÇAO
qtd = int(input())
for i in range(qtd):
    lista = []
    a, b = map(str, input().split())
    for i in range(min(len(a), len(b))):
        lista.append(a[0])
        lista.append(b[0])
        a = a[1:]
        b = b[1:]
    lista.append(a)
    lista.append(b)
    string = "".join(lista)
    print(string)
'''
#LIMEIRA SOLUCAO
qtd = int(input())
for i in range(qtd):
    lista = []
    a, b = map(str, input().split())
    minimo = min(len(a), len(b))
    maximo = max(len(a), len(b))
    for i in range(minimo):
        lista.append(a[i])
        lista.append(b[i])
    if len(a) > len(b):
        lista.append(a[len(b):])
    else:
        lista.append(b[len(a):])
    string = "".join(lista)
    print(string)
'''
