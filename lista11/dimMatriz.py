def calcula_dimensoes(matriz):
    lin = len(matriz)
    col = 1
    for i in matriz:
        col = len(i)
        break
    return "{}".format(lin) + "X" + "{}".format(col)

def dimensoes(matriz):
    print(calcula_dimensoes(matriz))

    
