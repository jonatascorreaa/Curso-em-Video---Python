#Faça um programa que lei um numero inteiro e mostre o seu sucessor e o seu antecessor
print('Esse é o programa que lê um numero inteiro e mostra o seu sucessor e seu antecessor. ', end = '\n')
N = int(input('Por favor digite um numero: '))
S = N + 1
A = N - 1
print('O numero escolhido foi {}. \nO seu sucessor é {} e o seu antecessor é {}' .format(N, S, A))
