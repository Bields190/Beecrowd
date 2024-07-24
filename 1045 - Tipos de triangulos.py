entrada = input()
ini = entrada.split()
num = []
for i in ini:
    num.append(float(i))
num.sort(reverse=True)
a = num[0]
b = num[1]
c = num[2]
if a>=(b+c):
    print("NAO FORMA TRIANGULO")
else:
    if (a*a)==((b*b)+(c*c)):
        print("TRIANGULO RETANGULO")
    elif (a*a)>((b*b)+(c*c)):
        print("TRIANGULO OBTUSANGULO")
    elif (a*a)<((b*b)+(c*c)):
        print("TRIANGULO ACUTANGULO")
    if a==b==c:
        print("TRIANGULO EQUILATERO")
    elif a==b or a==c or c==b:
        print("TRIANGULO ISOSCELES")