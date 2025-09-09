#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
#Dolar a 3,27 reais

print('\nEsse é o programa que mostra quantos dolares você pode comprar com reais')
r = float(input('Quantos reais você gostaria de converter? '))

d = 3.27
c = r // d
resto = r % d

print(f'Com {r} reais você consegue comprar {c:.0f} dolares e sobram {resto:.2f} reais')
