qtd = int(input())
for i in range(qtd):
    frase = input().split()
    for tamanho in range(len(frase)):
        if len(frase[tamanho]) >=10:
            if 'oulupukk' in frase[tamanho]:
                if '.' in frase[tamanho]:
                    frase[tamanho] = "Joulupukki."
                else:
                    frase[tamanho] = "Joulupukki"
    frase = " ".join(frase)
    print(frase)
