qtd = int(input())
texto = str(input())
a = texto.split()
coiso = []
for i in range(qtd):
#    coiso.append(a[i])
    if "UR" in a[i] and len(a[i]) < 4:
        a[i] = "URI"
    elif "OB" in a[i] and len(a[i]) < 4:
        a[i] = "OBI"
print(" ".join(a))
