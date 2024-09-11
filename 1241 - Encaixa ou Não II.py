num = int(input())
for i in range(num):
    A,B = map(str,input().split())
    azinho = A[len(A)-len(B):]
    if azinho == B:
        print("encaixa")
    else:
        print("nao encaixa")
#axe caralho tadakimasu porra deu certo