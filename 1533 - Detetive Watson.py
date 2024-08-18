while True:
    num = int(input())
    lista = []; lista2 = []
    if num == 0:
        break
    else:
        lista = list(map(int, input().split()))
        lista2 += lista
        aux = max(lista)
        lista.remove(aux)
        print(lista2.index(max(lista))+1)
