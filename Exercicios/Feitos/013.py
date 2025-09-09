#Faça um algoritimo que leia o salario de um funcionarioa e mostre seu novo salario com 15% de aumento
print('Esse é o programa que lê e reajusta seu salario com o aumento de 15%')
s = float(input('Qual o seu salario atual? R$'))
r = (s/100) * 15
print(f'O seu salario era de R${s}, agora você receberá R${s+r:.2f} com o reajuste')
