#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
#Dolar a 3,27 reais

print('\nEsse é o programa que mostra quantos dolares você pode comprar com reais')
r = int(input('Quanto você gostaria de converter? R$'))
c = r / 3.27
print(f'Com {r} reais você consegue comprar {c:.2f} dolares')
