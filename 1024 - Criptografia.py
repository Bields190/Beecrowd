qtd = int(input())
for vezes in range(qtd):
    linha = str(input())
    vetor = list(linha)
    for i in range(len(linha)):
        if vetor[i] .isalpha():
            vetor[i] = ord(vetor[i])+3
            vetor[i] = chr(vetor[i])
    vetor = vetor[::-1]
    vey = len(linha) // 2
    for j in range(vey, len(linha)):
        vetor[j] = ord(vetor[j])-1
        vetor[j] = chr(vetor[j])
    string = "".join(vetor)
    print(string)