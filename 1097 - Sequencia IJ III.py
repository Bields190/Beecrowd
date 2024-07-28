k = 5
for i in range(1, 10, 2):
    k += 2
    for j in range(k, k-3, -1):
        print(f'I={i} J={j}')
