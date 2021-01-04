n = int(input("Digite um número: "))

anterior = n % 10
n = n // 10
adjacentes = False

while n > 0 and not adjacentes:
    atual = n % 10
    if atual == anterior:
        adjacentes = True
    else:
        n = n // 10
        anterior = atual

if adjacentes:
    print("Esse número possui números adjacentes")
else:
    print("Esse número não possui números adjacentes")
