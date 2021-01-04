n = int(input("Digite o valor de n"))
k = int(input("Digite o valor de k"))

def fatorial(x):
    if (x==0):
        x = 1
        return x
    else:
        i = x-1
        while(i>0):
            x = x * i
            i -= 1
        return x

coefBin = fatorial(n) / (fatorial(k) * fatorial(n-k))

print(coefBin)
