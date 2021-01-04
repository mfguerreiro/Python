n = int(input("Digite o valor de n: "))
i = n - 1

if n == 0:
    n = 1
    
while(i > 0):
    n = n * i
    i-=1
print(n)
