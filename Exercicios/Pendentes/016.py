#Crie um programa que leia um numero real qualquer pelo teclado e mostra na sua tela a sua porção inteira
#Ex. O numero 6.127 tem a parte inteira 6
from math import trunc

print("\nEsse é o programa que lê um numero real e mostra a sua porção inteira.")
print("Ex. O numero 6.127 tem a parte inteira 6.")
numero = float(input("Digite um numero real: "))
parteinteira = trunc(numero)
print(f"A parte inteira é -{parteinteira}- e o seu numero foi {numero}")
