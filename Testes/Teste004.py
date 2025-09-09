import math

n = int(input("Digite um numero: "))
raiz = math.sqrt(n)
print(f"A raiz quadrada de {n} é igual a {math.ceil(raiz)}")

#Outra forma

from math import sqrt

num = int(input("Digite um numero: "))
r = sqrt(num)
print(f"A raiz quadrada de {n} é igual a {r:.2}")
