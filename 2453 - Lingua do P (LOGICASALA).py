linha = input().split()
resposta = []
for palavra in linha:
    resposta.append(palavra[1::2])
for i in range(len(resposta)):
    if i == len(resposta)-1:
        print(resposta[i])
    else:
        print(resposta[i], end=" ")
