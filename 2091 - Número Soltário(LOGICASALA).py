tam = int(input())
lista = []
vetor = list(map(int, input().split()))
#em que a entrada --> 1 3 4 3 1
#input().split() -> '1', '3', '4', '3', '1'
#map -------------> 1,3,4,3,1
#list ------------> [1, 3, 4, 3, 1]
for i in range(tam):
    if vetor[i] in lista:
        lista.remove(vetor[i])
    else:
        lista.append(vetor[i])
print(lista[0])
'''
FEITO EM SALA:::::
n = int(input())
while n != 0:
    linha = list(map(int, input().split()))
    pilha = []
    for item in lista:
        if item in lista:
            pilha.remove(item)
        else:
            pilha.append(item)
    print(pilha[0])
    n = int(input())
'''
