numeros = input()
lista = numeros.split()
num = []
for i in lista:
    num.append(int(i))
num.sort()
ver = (num[1]%num[0])
if ver == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")