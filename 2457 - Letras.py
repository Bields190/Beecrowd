letra = input()
texto = input()
vetor = texto.split()
qtd = 0
for i in range(len(vetor)):
    if letra in vetor[i]:
        qtd += 1
porcentagem = qtd*100/len(vetor)
print(f"{porcentagem:.1f}")
