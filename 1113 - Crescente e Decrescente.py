x = "0"
y = ""
while x != y:
    x, y = map(int, input().split())
    if x == y:
        exit()
    elif x > y:
        print("Decrescente")
    elif x < y:
        print("Crescente")
