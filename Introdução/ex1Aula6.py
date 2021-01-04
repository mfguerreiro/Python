n = int(input("Digite um número:"))
while n >= 0:
    if n == 0:
        print("1")
    else:
        fatorial = n
        i = n - 1
        while i > 1:
            fatorial = fatorial * i
            i -= 1
        print(fatorial)
    n = int(input("Digite um número:"))
