# Criar um iterador
iterador = iter('ABC')
# Qualquer iteravel pode ser percorrido com laço
for i in iterador:
    print(i)
# A função next só funciona em iterators
# print(next(iterador), next(iterador), next(iterador), next(iterador))

# Função que retorna iterador
alunos = ['Alice', 'Bernardo', 'Carlos']
it = enumerate(alunos) # O retorno é um iterador
# print(next(it))
for i in it:
    print(i)

reverso = reversed(alunos)
for i in reverso:
    print(i)

# Criar um dicionário a partir de um iterador
# Precisamos reiniciar o iterador
it = enumerate(alunos)
dicionario = dict(it)
print(dicionario)

for i in it:
    print(i)

numeros = [1, 2, 3, 4]
geradora = (i**2 for i in numeros)
combinacao = zip(numeros, geradora)
for item in combinacao:
    print(item)

# Caso sejam tamanhos diferentes, o zip vai parar de percorrer quando alcançar o ultimo elemento da menor coleção
