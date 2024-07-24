entrada = input()
lista = entrada.split()
num = []
for i in lista:
    num.append(int(i))
num.sort()
for i in num:
    print(i)
print("")
for i in lista:
    print(i)