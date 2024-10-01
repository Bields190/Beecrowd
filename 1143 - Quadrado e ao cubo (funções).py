def quadcubo(num):
    quad = num*num
    cubo = num*num*num
    print(f'{num} {quad} {cubo}')

qtd = int(input())
for i in range(1, qtd+1):
    quadcubo(i)
