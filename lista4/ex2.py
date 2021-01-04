def isPrimo(x):
    primo = True
    i = 3
    
    if x == 2 or x == 1:
      primo = True
    else:
      while i < x and primo == True:
        if x % i == 0:
            primo = False
    
        i += 1
       
    return primo
    
def maior_primo(n):
    maiorPrimo = 0
    
    while(n > 0):
        primo = isPrimo(n)
        if primo == True:
            maiorPrimo = n
            break
        else:
            n-=1
    return(maiorPrimo)