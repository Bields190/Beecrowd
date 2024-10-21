import sys

while True:
    try:
        entrada = input('Entre com um número: ')
        valor = int(entrada)
        if valor < 0:
            raise ValueError("Entrada não pode ser menor que zero!")
        x = 5 / int(valor)
        print(x)
    except ValueError as erro:
        # print(f"Erro: {sys.exc_info()}")
        print(str(erro))
        print("Tente novamente.")
    except ZeroDivisionError as zde:
        #print(f"{sys.exc_info()}")
        print("Não é possível fazer divisão por zero.\nTente novamente.")
    except (EOFError, KeyboardInterrupt) as eor:
        print("Fim do programa...")
    finally:
        print(f"A entrada foi '{entrada}'")


