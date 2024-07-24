n = int(input())
ino = 0
out = 0
for i in range(0,n,1):
    aux = int(input())
    if aux >= 10 and aux <= 20:
        ino += 1
    else:
        out +=1
print(f"{ino} in")
print(f"{out} out")