n1, n2, n3, n4 = map(float, input().split())
m1 = n1*2
m2 = n2*3
m3 = n3*4
m4 = n4*1
mediain = (m1+m2+m3+m4)/10
if mediain >= 7.0:
    print(f"Media: %.1f"%mediain), print("Aluno aprovado.")
elif mediain < 5.0:
    print(f"Media: %.1f"%mediain), print("Aluno reprovado.")
else:
        exame = float(input())
        print(f"Media: %.1f"%mediain), print("Aluno em exame.")
        print(f"Nota do exame: %.1f"%exame)
        final = (mediain + exame)/2
        if final >= 5.0:
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")
        print(f'Media final: %.1f'%final)