print('\nEsse é o programa que lê um numero inteiro e mostra a sua tabuada')
n = int(input('Digite um numero: '))

print('\nDivisão:')
for i in range(1,11):
    resultado = n / i
    print(f'{n} / {i} = {resultado:.3f}')
