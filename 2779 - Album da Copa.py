total_fig = int(input())
compradas = int(input())
figs = []
for i in range(1, total_fig+1):
    figs.append(i)
for i in range(compradas):
    elemento = int(input())
    if elemento in figs:
        figs.remove(elemento)
    else:
        continue
print(len(figs))
