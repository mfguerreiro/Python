def dimensoes(matriz):
    lin = len(matriz)
    col = 1
    for i in matriz:
        col = len(i)
        break
    return lin, col


def soma_matrizes(m1,m2):
    lin, col = dimensoes(m1)
    if dimensoes(m1) != dimensoes(m2):
        return False
    else:
        m3 = m1
        for i in range(0, lin):
            for j in range(0, col):
                m3[i][j] = m1[i][j] + m2[i][j]
        return m3
