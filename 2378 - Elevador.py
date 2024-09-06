N, C = map(int, input().split())
tot = 0; var = 0
for i in range(N):
    S, E = map(int, input().split())
    tot -= S
    tot += E
    if tot > C:
        var += 1
if var >= 1:
    print('S')
else:
    print('N')