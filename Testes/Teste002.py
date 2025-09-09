#Usar o f-strings (f"{variavel}") deixa o codigo mais limpo que a função .format()

#Usando o f-strings (f"{variavel}"):
n = 'Jonatas'
i = 22
print(f'Meu nome é {n} e eu tenho {i} anos\n')

#Usando o .format()
n = 'Pedro'
i = 30
print('Meu nome é {} e eu tenho {} anos\n'.format(n, i))


#Outra variação do f-strings (f"{variavel}"):
n1 = 'Paulo'
n2 = 'João'
i1 = 20
i2 = 30
print(f'Eu sou o {n1} e tenho {i1} anos, meu irmão se chama {n2} e tem {i2} anos, juntos nós temos {i1 + i2} anos\n')

#agora utilizando o .format()
n1 = 'Paulo'
n2 = 'João'
i1 = 20
i2 = 30
print('Eu sou o {} e tenho {} anos, meu irmão se chama {} e tem {} anos, juntos nós temos {} anos\n'.format(n1, i1, n2, i2, i1 + i2))
#Aqui tambem poderia criar uma nova variavel do tipo s = i1 + i2, o que ocuparia mais uma linha de espaço
