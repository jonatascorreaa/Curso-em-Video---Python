a = input("Digite algo: ")
#print("O tipo primitivo desse valor é: ", type(a))
#print("Só tem espaços? ", a.isspace())
#print("É um numero? ", a.isnumeric())
#print("É um alfabetico? ", a.isalpha())
#print("É um alfanumerico? ", a.isalnum())
#print("Está em minusculas? ", a.islower())

if type(a) == str:
    print("É uma String")
else:
    print("Deu errado")


if a.isspace() is True:
    print("Tem somente espaços")
else:
    print("Não tem somente espaços")


if " " in a:
    print("Possui espaços")
    # Necessita de consertos


if a.isnumeric() is True:
    print("É um numero")
else:
    print("Não é um numero")

