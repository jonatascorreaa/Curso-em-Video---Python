#Faça um programa que leia um angulo qualquer e mostre o valor do seu seno, cosseno e tangente desse angulo
import math

#Script/Coleta de dados
print("\nEsse é o programa que lê um angulo qualquer e mostra o seu Seno, o seu Cosseno e a sua Tangente")
angulo = float(input("Qual o valor do angulo? "))

#Transormando angulos X para Radianos
radiano = math.radians(angulo)

#Calculo do Sen, Cos e Tan
seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

#Resultado
print(f"O angulo que pediu foi {angulo}. O seu Seno é igual a {seno:.4f}. O seu Cosseno é igual a {cosseno:.4f}. A sua Tangente é igual a {tangente:.4f}")
