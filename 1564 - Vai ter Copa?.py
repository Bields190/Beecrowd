while True:
    try:
        n = int(input())
        if n > 0:
            print("vai ter duas!")
        elif n == 0:
            print("vai ter copa!")
    except EOFError:
        break