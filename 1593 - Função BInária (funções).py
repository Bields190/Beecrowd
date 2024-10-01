def contBin(num):
    nario = bin(num)

    return nario.count('1')


qtd = int(input())
for i in range(qtd):
    numero = int(input())
    print(contBin(numero))
