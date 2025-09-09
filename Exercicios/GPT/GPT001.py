def converter_medida(valor, unidade_origem, unidade_destino):
    fatores = {
        'mm': 1,
        'cm': 10,
        'dm': 100,
        'm': 1000,
        'dam': 10000,
        'hm': 100000,
        'km': 1000000
    }

    if unidade_origem not in fatores or unidade_destino not in fatores:
        print("Unidade inválida. Tente novamente.")
        return

    valor_convertido = valor * (fatores[unidade_origem] / fatores[unidade_destino])
    print(f"{valor}{unidade_origem} convertido para {unidade_destino} é igual a {valor_convertido}{unidade_destino}")


# Programa principal
print("Este é o programa conversor de medidas.")
print(
    "Válido para Milímetros (mm), Centímetros (cm), Decímetros (dm), Metros (m), Decâmetros (dam), Hectômetros (hm), Quilômetros (km)")

n1 = input("Qual a primeira medida que você irá usar? Use a abreviação: ").strip().lower()
n2 = input("Para qual medida você quer converter? ").strip().lower()

if n1 == n2:
    print(f"O valor em {n1} já está em {n2}. Tente novamente.")
else:
    try:
        valor = float(input(f"Qual é o valor em {n1}? "))
        converter_medida(valor, n1, n2)
    except ValueError:
        print("Por favor, insira um número válido.")
