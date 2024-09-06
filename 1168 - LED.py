leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
qtd = int(input())
for i in range(qtd):
    x = input()
    soma = 0
    lista = list(x)
    for i in range(len(lista)):
        lista[i] = int(lista[i])
#    for j in range(10):
#        if j in lista:
#            while lista.count(j) > 1:
#                lista.remove(j)
    for i in lista:
        soma += leds[int(i)]
    print(f'{soma} leds')