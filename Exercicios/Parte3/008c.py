print('Este é o programa conversor de medidas.', end = '\n')
print('Valido para Milimetros (mm), Centimetros (cm), Decimetros (dm)', end = '')
print(', metros (m), Decametro (dam), Hectometro (hm), kilometro (km)')

n1 = str(input('Qual a primeira medida que você irá usar? Use a abreviação: '))
n2 = str(input('Para qual medida você quer converter? '))

#mm  cm  dm  m  dam  hm  km

if n1 == n2:
    print('O valor em <{}> já está em <{}>. Tente novamente.'.format(n1, n2))

if n1 == 'mm' and n2 == 'cm' or n1 == 'cm' and n2 == 'dm' or n1 == 'dm' and n2 == 'm' or n1 == 'm' and n2 == 'dam' or n1 == 'dam' and n2 == 'hm' or n1 == 'hm' and n2 == 'km':
    m1 = float(input('Qual é o primeiro valor em {}?: '.format(n1)))
    r = m1 / 10
    print('{}{} convetido em {} é igual a {}{}'.format(m1, n1, n2, r, n2))

if n1 == 'km' and n2 == 'hm' or n1 == 'hm' and n2 == 'dam' or n1 == 'dam' and n2 == 'm' or n1 == 'm' and n2 == 'dm' or n1 == 'dm' and n2 == 'cm' or n1 == 'cm' and n2 == 'mm':
    m1 = float(input('Qual é o primeiro valor em {}?: '.format(n1)))
    r = m1 * 10
    print('{}{} convertido em {} é igual a {}{}'.format(m1, n1, n2 , r, n2))

#mm  cm  dm  m  dam  hm  km

if n1 == 'mm' and n2 == 'dm' or n1 == 'cm' and n2 == 'm' or n1 == 'dm' and n2 == 'dam' or n1 == 'm' and n2 == 'hm' or n1 == 'dam' and n2 == 'km':
    m1 = float(input('Qual o primeiro valor em {}?: '.format(n1)))
    r = m1 / 100
    print('{}{} convertido em {} é igual a {}{}'.format(m1, n1, n2, r, n2))

if n1 == 'km' and n2 == 'dam' or n1 == 'hm' and n2 == 'm' or n1 == 'dam' and n2 == 'dm' or n1 == 'm' and n2 == 'cm' or n1 == 'dm' and n2 == 'mm':
    m1 = float(input('Qual o primeiro valor em {}?: '.format(n1)))
    r = m1 * 100
    print('{}{} convertido em {} é igual a {}{}'.format(m1, n1, n2, r, n2))

#mm  cm  dm  m  dam  hm  km

if n1 == 'mm' and n2 == 'm' or n1 == 'cm' and n2 == 'dam' or n1 == 'dm' and n2 == 'hm' or n1 == 'm' and n2 == 'km':
    m1 = float(input('Qual o primeiro valor em {}?: '.format(n1)))
    r = m1 / 1000
    print('{}{} convertido em {} é igual a {}{}'.format(m1, n1, n2, r, n2))

if n1 == 'km' and n2 == 'm' or n1 == 'hm' and n2 == 'dm' or n1 == 'dam' and n2 == 'cm' or n1 == 'm' and n2 == 'mm':
    m1 = float(input('Qual o primeiro valor em {}?: '.format(n1)))
    r = m1 * 1000
    print('{}{} convertido em {} é igual a {}{}'.format(m1, n1, n2, r, n2))

#mm  cm  dm  m  dam  hm  km

if n1 == 'mm' and n2 == 'dam' or n1 == 'cm' and n2 == 'hm' or n1 == 'dm' and n2 == 'km':
    m1 = float(input('Qual o primeiro valor em {}?: '.format(n1)))
    r = m1 / 10000
    print('{}{} convertido em {} é igual a {}{}'.format(m1, n1, n2, r, n2))

if n1 == 'km' and n2 == 'dm' or n1 == 'hm' and n2 == 'cm' or n1 == 'dam' and n2 == 'mm':
    m1 = float(input('Qual o primeiro valor em {}?: '.format(n1)))
    r = m1 * 10000
    print('{}{} convertido em {} é igual a {}{}'.format(m1, n1, n2, r, n2))

#mm  cm  dm  m  dam  hm  km

if n1 == 'mm' and n2 == 'hm' or n1 == 'cm' and n2 == 'km':
    m1 = float(input('Qual o primeiro valor em {}?: '.format(n1)))
    r = m1 / 100000
    print('{}{} convertido em {} é igual a {}{}'.format(m1, n1, n2, r, n2))

if n1 == 'km' and n2 == 'cm' or  n1 == 'hm' and n2 == 'mm':
    m1 = float(input('Qual o primeiro valor em {}?: '.format(n1)))
    r = m1 * 100000
    print('{}{} convertido em {} é igual a {}{}'.format(m1, n1, n2, r, n2))

#mm  cm  dm  m  dam  hm  km

if n1 == 'mm' and n2 == 'km':
    m1 = float(input('Qual o primeiro valor em {}?: '.format(n1)))
    r = m1 / 1000000
    print('{}{} convertido em {} é igual a {}{}'.format(m1, n1, n2, r, n2))

if n1 == 'km' and n2 == 'mm':
    m1 = float(input('Qual o primeiro valor em {}?: '.format(n1)))
    r = m1 * 1000000
    print('{}{} convertido em {} é igual a {}{}'.format(m1, n1, n2, r, n2))
