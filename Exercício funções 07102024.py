from functools import reduce
Fatura = [('Net', 199.9), ('Ifood', 999.87), ('Gasolina', 678.0), ('Formigão', 400)]


def formatar(x):
    for i in x:
        print(f"{i[0]} - R${i[1]}")
def somar(x):
    soma = 0
    for i in x:
        soma +=i[1]
    return soma

print("1º:")
formatar(Fatura)
print("\n 2º:")
Fatura.sort(key=lambda x: x[1], reverse=True)
formatar(Fatura)
print("\n 3º:")
print(list(filter(lambda x: x[1] > 500, Fatura)))
print("\n 4º:")
print(f"Total da Fatura: {somar(Fatura)}")