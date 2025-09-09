# Escreva um programa que pergunte a quantidade de km percorrido por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar. O carro custa R$60 por dia e R&0.15 por km rodado

print('\nEsse é o programa que calcula o preço a ser pago pela utilização do carro alugado')
d = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos km você percorreu com o veiculo? '))

pago = (d * 60) + (km *0.15)

print(f'Você ficou com o carro por {d} dias e andou {km}km, o valor total a pagar será de R${pago:.2f}')
