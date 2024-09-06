maior = 0
palavrao = ""
while True:
    pal = input().split()
    if pal[0] == '0':
        print()
        break
    else:
        for i in range(len(pal)):
            if len(pal[i]) >= maior:
                maior = len(pal[i])
                palavrao = pal[i]
            if i == len(pal) - 1:
                print(f'{len(pal[i])}')
            else:
                print(f'{len(pal[i])}', end="-")
print(f'The biggest word: {palavrao}')
