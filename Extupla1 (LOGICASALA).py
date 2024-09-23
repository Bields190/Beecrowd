#ENTRADA: (1,2,3) (4,5,6,7,8)
#Converter em uma lista

s1, s2 = input().split()
t1 = tuple(map(int,  s1.replace('(', '').replace(')', '').split(',')))
t2 = tuple(map(int,  s2.replace('(', '').replace(')', '').split(',')))
lista = []
if len(t1) <= len(t2):
    for i in range(len(t1)):
        lista.append(t1[i])
        lista.append(t2[i])
    for i in range(len(t1), len(t2)):
        lista.append(t2[i])
else:
    for i in range(len(t2)):
        lista.append(t2[i])
        lista.append(t1[i])
    for i in range(len(t1)):
        lista.append(t1[i])
print(tuple(lista))

'''a, b = map(str, input().split(" "))
a = a.split(',')
b = b.split(',')
for x in range(len(a)):
    a[x] = int(a[x])
for x in range(len(b)):
    b[x] = int(b[x])
print(a, b)
lista = []

for i in range(0, min(len(a), len(b))-1):
    lista.append(a[i])
    lista.append(b[i])
    
lista += a
lista += b
print(lista)
'''