num = -0.2
while num < 1.6:
    num += 0.2
    for i in range(1, 4, 1):
        if num.is_integer():
            print(f"I={int(num)} J={int(i + num)}")
        else:
            print(f"I={num:.1f} J={i+num:.1f}")
for i in range(3, 6, 1):
    print(f"I=2 J={i}")