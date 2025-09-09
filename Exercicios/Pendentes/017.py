#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo e calcule e mostre o comprimento da hipotenusa
import math

#Script/Coleta de dados
print("\nEsse é o programa que lê o comprimento do cateto oposto e do cateto adjacente\nde um triangulo retangulo" \
" e mostra a sua hipotenusa")
co = float(input("Qual o comprimento do Cateto Oposto? "))
ca = float(input("Qual o comprimento do Cateto Adjacente? "))

#Função que eleva ao quadrado
co2 = math.pow(co, 2)
ca2 = math.pow(ca, 2)

#Calculo da Hipotenusa
hipotenusa2 = co2 + ca2
hipotenusa = math.sqrt(hipotenusa2)

#Resultado
print(f"A hipotenusa é igual a {hipotenusa}")
