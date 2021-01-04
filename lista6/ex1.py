largura = int(input("Digite a largura:"))
altura = int(input("Digite a altura:"))
contLargura = 0
contAltura = 0

while contAltura < altura:
    while contLargura < largura:
        print("#", end="")
        contLargura += 1
    print()
    contAltura += 1
    contLargura = 0
