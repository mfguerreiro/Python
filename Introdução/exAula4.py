num = int(input("Digite um número para saber a soma dos dígitos: "))
soma = 0
while num > 0:
    soma = soma + (num % 10)
    num = num // 10

print("Soma dos dígitos:", soma)
