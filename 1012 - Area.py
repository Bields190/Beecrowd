val = input().split()
a = float(val[0])
b = float(val[1])
c = float(val[2])
tri = (a*c)/2
cir = 3.14159 * (c*c)
trap = (a+b)*(c/2)
qua = b*b
ret = a*b
print(f'TRIANGULO: %.3f'%tri)
print(f'CIRCULO: %.3f'%cir)
print(f'TRAPEZIO: %.3f'%trap)
print(f'QUADRADO: %.3f'%qua)
print(f'RETANGULO: %.3f'%ret)