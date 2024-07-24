par = 0
imp = 0
pos = 0
neg = 0
for i in range (0, 5):
    var = int(input())
    if var%2 == 0:
        par += 1
    else:
        imp += 1
    if var>0:
        pos += 1
    elif var < 0:
        neg += 1

print(f"{par} valor(es) par(es)")
print(f"{imp} valor(es) impar(es)")
print(f"{pos} valor(es) positivo(s)")
print(f"{neg} valor(es) negativo(s)")