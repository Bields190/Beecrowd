num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Nova lista com elementos ao quadrado:
quadrado = [item*item for item in num]
print(f'Lista de quadrados: ', quadrado)

# Lista apenas com os números pares:
pares = [i for i in num if i % 2 == 0]
print(f'Lista de Pares: ', pares)

# Lista com pares e quadrados impares
lista = [i if i % 2 == 0 else i*i for i in num]
print(f'Lista de pares e quadrados: ', lista)

let = ['a', 'b', 'c']

# Lista que combina todas as letras com os números:

com = [(l, n) for l in let for n in num]
print(f'Lista de combinações: ', com)

# Uma matriz de 3 linhas e 4 colunas:
mat = [[j+1+i*3 for j in range(3)] for i in range(4)]
print(f'Matriz: ', mat)

# Transposta:
'''mat2 = []
for j in range(4):
    linha = []
    for i in range(3):
        linha.append(j+1+i*4)
    mat2.append(linha)'''

mat2 = [[j+1+i*4 for i in range(3)] for j in range(4)]
print(f'Matriz Transposta: ', mat2)

# Usando Strings:
frutas = [' abacate', ' banana ', 'abacaxi ']
novas_frutas = None
print(f'Frutas: ', novas_frutas)

#SET:
frase = 'Exemplo de set comprehension'
todas_vogais = [i for i in frase if i in 'aeiou']
unicas_vogais = {i for i in frase if i in 'Eaeiou'}
print(f'Todas Vogais: ', todas_vogais)
print(f'Unicas Vogais: ', unicas_vogais)
#Dicionário:
vogais_dict = {i:frase.count(i) for i in frase if i in 'aeEiou'}
print(f"Dicionarizado: ", vogais_dict)
#Gerar uma função geradora
geradora = (i*i for i in num)
print(geradora)
for g in geradora:
    print(g)
