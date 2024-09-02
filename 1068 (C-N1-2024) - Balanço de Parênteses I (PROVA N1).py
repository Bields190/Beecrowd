while True:
    try:
        ex = []
        expressao = input()
        if expressao[0] == ")" or expressao[len(expressao)-1] == "(":
            print("incorrect")
        elif expressao.count("(") == expressao.count(")"):
            print("correct")
        else:
            print("incorrect")
    except EOFError:
        break
