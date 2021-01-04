largura = int(input("Digite a largura:"))
altura = int(input("Digite a altura:"))
contLargura = 1
contAltura = 1

while contAltura <= altura:
    while contLargura <= largura:
        if contAltura == 1 or contAltura == altura :
            print("#", end="")
        else:
            if contLargura == 1 or contLargura == largura :
                print("#", end="")
            else:
                print(" ", end="")
            
        contLargura += 1
    print()
    contAltura += 1
    contLargura = 1
