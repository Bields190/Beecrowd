while True:
    try:
        linha = input()
        pilha = []
        status = True
        for i in linha:
            if i == '(':
                pilha.append(i)
            elif i == ')':
                if len(pilha) > 0:
                    pilha.pop()
                else:
                    status = False
        if status == True and len(pilha) == 0:
            print("correct")
        else:
            print("incorrect")
    except EOFError:
        break