#Faça um programa que leia temperaturas e converta elas, entre C, F e K

print('\nEsse é o programa de conversão de temperaturas')
t = str(input('Você quer converter graus Celcius, Fahrenheit ou Kelvin? '))
v = float(input('Qual a temperatura? '))
if t not in ['Celcius' , 'Fahrenheit', 'Kelvin']:
    print('\nO nome está errado, tente novamente.')
    exit()

if t == 'Celcius':
    c = v
    f = (c * 1.8) + 32
    k = c + 273.15
    print(f'A temperatura de {v}ºC é igual a {f}ºF e {k:.0f}K')

if t == 'Fahrenheit':
    f = v
    c = (f - 32) * 5 / 9
    k = (f - 32) * 5 / 9 + 273.15
    print(f'A temperatura de {f}ºF é igual a {c}ºC e {k:.2}K')

if t == 'Kelvin':
    k = v
    c = k - 273.15
    f = (k - 273.15) * 9 / 5 + 32
    print(f'A temperatura de {k}K é igual a {c:.2f}ºC e {f:.2f}ºF')
