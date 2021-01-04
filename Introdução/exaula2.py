import math
a = float(input("Valor a:"))
b = float(input("Valor b:"))
c = float(input("Valor c:"))

delta = (b**2) -(4 * a * c)

if (delta < 0):
  print("Não possui raiz")
elif (delta == 0):
  raiz1 = (- b) / (2 * a)
  print("Raiz única =", raiz1)
else:
  raiz1 = (- b + math.sqrt(delta)) / (2 * a)
  raiz2 = (- b - math.sqrt(delta)) / (2 * a)
  print("Raiz1 =", raiz1, "\nRaiz2 =", raiz2)
