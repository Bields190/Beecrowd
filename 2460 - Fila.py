fila = []; desistentes = []
qtdin = int(input())
fila = list(map(int, input().split()))
qtdsai = int(input())
desistentes = list(map(int, input().split()))
for i in range(0, qtdsai):
    if desistentes[i] in fila:
        fila.remove(desistentes[i])
for i in range(0, qtdin-qtdsai-1):
    print(fila[i], end=" ")
print(fila[qtdin-qtdsai-1])