alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
qtd = int(input())
for i in range(qtd):
    mais = 0
    frase = input()
    lista = list(frase)
    for j in range(len(alfabeto)):
        if alfabeto[j] in lista:
            mais += 1
            for x in range(lista.count(alfabeto[j])):
                lista.remove(alfabeto[j])
    if mais == 26:
        print("frase completa")
    elif mais >= 26/2:
        print("frase quase completa")
    else:
        print("frase mal elaborada")
