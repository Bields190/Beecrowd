import time
tamanho = 10**8

# Função Geradora:


def gera(t):
    for i in range(t):
        yield (i*i)


# Função com Loop interativo:
def loop(tamanho):
    lista = []
    for i in range(tamanho):
        lista.append(i*i)
    return lista

# Função com list-comprehension:


def listc(tamanho):
    return [i*i for i in range(tamanho)]



inicio = time.time()
loop(tamanho)
fim = time.time()
print(round(fim - inicio, 3))
inicio = time.time()
listc(tamanho)
fim = time.time()
print(round(fim - inicio, 3))
inicio = time.time()
for i in gera(tamanho):
    continue
fim = time.time()
print(round(fim - inicio, 3))
