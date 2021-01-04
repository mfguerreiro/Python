#def inverter(lista):
#    nova_lista = []
#    for i in lista:
#        if i not in nova_lista:
#            nova_lista.append(i)
#    return sorted(nova_lista)
        
n = 1
lista = []
while n != 0:
    n = int(input("Digite um número:"))
    lista.append(n)

x = len(lista) - 1 
while x >= 0:
    if lista[x] != 0:
        print(lista[x])
    x -=1
