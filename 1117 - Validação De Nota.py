qtd = 0
soma = 0
while qtd!= 2:
    nota = float(input())
    if nota < 0 or nota > 10:
        print("nota invalida")
    else:
        qtd += 1
        soma += nota
media = soma / qtd
print(f"media = {media:.2f}")