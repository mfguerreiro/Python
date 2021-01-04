def partida():
    n = int(input("Quantas peças?"))
    m = int(input("Limite de peças por jogada?"))

    turno = 0 # 1 para computador 2 para usuario
    vencedor = 0 # 1 para computador 2 para usuario
    if n % (m+1)  == 0:
        print("\nVocê começa!\n")
        turno = 2
    else:
        print("\nComputador começa!\n")
        turno = 1
    while n != 0:
        if turno == 2:
            jogada = usuario_escolhe_jogada(n, m)
            n = n - jogada
            if jogada == 1:
                print("\nVoce tirou uma peça.")
            else:
                print("\nVoce tirou", jogada, "peças.")

            if n == 0: # RESTAM PEÇAS
                print("Fim do jogo! Voce ganhou!")
                vencedor = 2
                return vencedor
            elif n == 1:
                print("Agora resta apenas uma peça no tabuleiro.\n")
            else:
                print("Agora restam", n , " peças no tabuleiro.\n")
            turno = 1

        elif turno == 1:
            jogada = computador_escolhe_jogada(n, m)
            n = n - jogada
            if jogada == 1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou", jogada, "peças.")

            if n == 0: # RESTAM PEÇAS
                print("Fim do jogo! O computador ganhou!")
                vencedor = 1
                return vencedor
            elif n == 1:
                print("Agora resta apenas uma peça no tabuleiro.\n")
            else:
                print("Agora restam", n , " peças no tabuleiro.\n")
            turno = 2

def campeonato():
    i = 1
    computador = 0
    usuario = 0
    while i<=3:
        print("\n**** Rodada",i,"****\n")
        resultado = partida()
        if resultado == 1:
            computador +=1
        else:
            usuario +=1
        i+=1

    print("\n**** Final do campeonato! ****\n\nPlacar: Você ",usuario," X ",computador," Computador ")

def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    else:
        quantia = n % (m+1)

        if quantia > 0:
            return quantia
        else:
            return m


def usuario_escolhe_jogada(n, m):
    retirar = 0
    valido = False
    while valido == False:
        retirar = int(input("Quantas peças você vai tirar?"))
        if retirar >= 1 and retirar <= m and retirar <= n:
            valido == True
            return retirar
        else:
            print("\nOops! Jogada inválida! Tente de novo.\n")

##################################################################################################################

# MENU INICIAL

print("Bem-vindo ao jogo do NIM! Escolha: \n\n1 - para jogar uma partida isolada \n2 - para jogar um campeonato")

escolhe = int(input())
if escolhe == 1:
    print("Voce escolheu uma partida isolada!")
    partida()
elif escolhe == 2:
    print("Voce escolheu um campeonato!")
    campeonato()
else:
    print("Valor incorreto, tente novamente:")
