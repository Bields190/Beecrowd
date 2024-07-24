a, b, c = map(float, input().split())
if a+b>c and a+c>b and b+c>a:
    per = a+b+c
    print(f"Perimetro = %.1f"%per)
else:
    area = (a+b)*(c/2)
    print(f"Area = %.1f"%area)