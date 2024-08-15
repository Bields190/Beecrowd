
notas = [0]*101
maior = 0
pos = 0
qtd = int(input())
quant = list(map(int, input().split()))
for i in range(0, 101):
    for j in range(0, qtd):
        if quant[j] == i:
            notas[i] += 1
for i in range(len(notas)):
    if notas[i] >= maior:
        pos = i
        maior = notas[i]

print(pos)

#entao vai se fuder vai se fuder vai pro caralho vai tomar no cu n consegui fazer a porra da lógica da saída dessa buceta desse caralho de lógica facil mas nada eh facil pro pitón n eh mesmo vou smt na minha própria frente as 11:00 pq eh o horário q acaba a aula na vdd n eh as 11 eh as 11:10 af odiei #desabafei #faleitoleve #gaysmorrendo #desinclusao #autohomofobia
#deu certo amo minha vida tudo e todes eu amo todo mundo deu tipo super certo nossa as coisa aq tao tudo ficando verde af scr
'''
x = int(input())
frequencia = [0] * 101
linha = input().split()
for i in range(len(linha)):
    nota = int(linha[i])
    frequencia[nota] += 1
maior = 0
posicao = 0
for j in range(len(frequencia)):
    if maior <= frequencia[j]:
        posicao = j
        maior = frequencia[j]
print(posicao)
'''
