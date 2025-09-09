print('Esse é o programa que lê um numero e mostra o seu dobro, triplo e sua raiz quadrada')
n = int(input("Por favor, digite um numero: "))
print(f' O numero escolhido foi {n}\nO Seu dobro é {n*2}\nO seu triplo é {n*3}', end = '')
print(f'\nA sua raiz quadrada é {n**(1/2):.2f}')
