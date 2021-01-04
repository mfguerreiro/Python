def calcula_linha(matriz):
    lin = len(matriz)
    return lin

def calcula_coluna(matriz):
    col = 1
    for i in matriz:
        col = len(i)
        break
    return col

def imprime_matriz(matriz):
    lin = calcula_linha(matriz)
    col = calcula_coluna(matriz)

    for i in range(0, lin):
        for j in range(0, col):
            if(j == col - 1):
                print(matriz[i][j], end="")
            else:
                print(matriz[i][j], end=" ")
        print()
