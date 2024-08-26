num = int(input())
linha = []
for i in range(num):
    linha.append(int(input()))
campo = [0]*num
for i in range(num):
    campo[i] += linha[i]
    if i > 0:
        campo[i] += linha[i-1]
    if i < num-1:
        campo[i] += linha[i+1]
for i in range(num):
    print(campo[i])
