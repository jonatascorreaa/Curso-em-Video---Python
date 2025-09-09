#Faça um programa que leia um numero inteiro qualquer e mostre na sua tela a sua tabuada
print('\nEsse é o programa que lê um numero inteiro e mostra a sua tabuada')
n = int(input('Digite um numero: '))

print('\nAdição:')
for i in range(1,11):
    resultado = n + i
    print(f'{n} + {i} = {resultado}')

print('\nSubtração:')
for i in range(1,11):
    resultado2 = n - i
    print(f'{n} - {i} = {resultado2}')

print('\nMultiplicação:')
for i in range(1,11):
    resultado3 = n * i
    print(f'{n} * {i} = {resultado3}')

print('\nDivisão:')
for i in range(1,11):
    resultado4 = n / i
    print(f'{n} / {i} = {resultado4:.2f}')
