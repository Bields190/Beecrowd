n = int(input())
for i in range(1, n+1, 1):
    var = int(input())
    if var == 0:
        print("NULL")
    else:
        if var%2 == 0:
            print("EVEN", end=" ")
        else:
            print("ODD", end=" ")
        if var>0:
            print("POSITIVE")
        else:
            print("NEGATIVE")