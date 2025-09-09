#Escreva um programa que leia o valor em metros e exibe ele em centimetros e milimetros
print('Este é o programa que lê um valor em metros e transforma em ', end='')
print('centimetros e milimetros')
n = float(input('Digite o valor, em metros, que você quer converter: '))
c = n * 100
m = c * 10
print('O valor que você informou foi {} \nEsse valor equivale a {}cm e {}mm'.format(n, c, m))
