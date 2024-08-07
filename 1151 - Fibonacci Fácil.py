a = int(input())
an1 = 0
an2 = 1
print(an1, an2, end=" ")
for i in range(a-3):
    prox = (an1+an2)
    print(prox, end= " ")
    an1 = an2
    an2 = prox
print(an1+an2)