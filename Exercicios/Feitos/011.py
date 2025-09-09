#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua area e a quantidade de tinta necessaria para pinta-la
#Sabendo que cada lata de tinta pinta uma area de 2m² quadrados

print('\nEsse é o programa que lê as medidas de uma parede e determina a quantidade necessaria de latas para pinta-lá')
print('Considera-se que uma lata pinta 2m²')
print('Use a medida em metros')

largura = float(input('\nQual a largura da parede? '))
altura = float(input('Qual a altura da parede? ' ))

area = largura * altura
tinta = area/2

print(f'A sua parede possui {area:.2f}m², para pinta-lá será necessario {tinta:.1f} latas de tinta')
