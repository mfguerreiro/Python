num = int(input("Digita um número inteiro: "))
soma = 0
while num > 0:
    anterior = num % 10
    soma = soma + anterior
    num = num // 10

print(soma)
