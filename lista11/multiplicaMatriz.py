def calcula_linha(matriz):
    lin = len(matriz)
    return lin

def calcula_coluna(matriz):
    col = 1
    for i in matriz:
        col = len(i)
        break
    return col

def sao_multiplicaveis(m1, m2):
    lin1 = calcula_linha(m1)
    col1 = calcula_coluna(m1)
    lin2 = calcula_linha(m2)
    col2 = calcula_coluna(m2)

    if col1 != lin2:
        return False
    else:
        return True

    
