# Exercicio 11

print('\nEsse é o programa que lê as medidas de uma parede e determina a quantidade necessária de latas para pintá-la.')
print('Considera-se que uma lata pinta 2m².')
print('Use a medida em metros.')

# Entrada de dados
largura = float(input('\nQual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))

# Cálculo da área
area = largura * altura
tinta = area / 2  # Divide corretamente a área pelo rendimento de cada lata

# Verifica se precisa arredondar para cima
if tinta % 1 != 0:  # Se o número não for inteiro, precisa de uma lata extra
    latas = int(tinta) + 1  # Arredonda manualmente somando 1
    sobra = (latas * 2) - area  # Calcula a sobra de tinta
    print(f'A parede possui {area:.2f}m², para pintá-la será necessário {latas} latas e restará {sobra:.2f}m² de tinta em uma lata.')
else:
    latas = int(tinta)  # Apenas pega a parte inteira
    print(f'A parede possui {area:.2f}m², para pintá-la será necessário {latas} latas de tinta, não irá sobrar nada.')
