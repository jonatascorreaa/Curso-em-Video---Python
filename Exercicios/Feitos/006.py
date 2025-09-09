#Crie um algoritimo que leia um numero e mostre o seu dobro, triplo e sua raiz quadrada
print('Esse é o programa que lê um numero e mostra o seu dobro, triplo e sua raiz quadrada')
n = int(input("Por favor, digite um numero: "))
d = n * 2
t = n * 3
r = n ** (1/2)
print(' O numero escolhido foi {}\nO Seu dobro é {}\nO seu triplo é {}'.format(n, d, t), end = '')
print('\nA sua raiz quadrada é {:.2f}'.format(r))
