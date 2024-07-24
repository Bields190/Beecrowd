a, b, c = map(float,input().split())
delta = (((b*b)-4*a*c))
raiz = delta**0.5
if delta <= 0 or (a==0):
    print("Impossivel calcular")
else:
    x1 = (((-b)+raiz)/(2*a))
    x2 = (((-b)-raiz)/(2*a))
    print(f'R1 = %.5f'%x1)
    print(f'R2 = %.5f'%x2)