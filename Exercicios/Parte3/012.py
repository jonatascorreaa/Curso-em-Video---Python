#Faça um algoritimo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto
print('Esse é o programa que calcula o desconto de um produto:')
p = float(input('Qual o valor do produto? R$'))
d = (p/100) * 5
v = p - d
print(f'O valor dito foi {p:.2f}, onde teve o desconto de {d:.2f} reais, custando {v:.2f} reais')
