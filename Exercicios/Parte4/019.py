#Um professor quer sortear um dos seus 4 alunos para apagar o quadro Faça um programa que ajude ele, lendo o nome deles e falando o nome do escolhido.
import random

#Script
print("Esse é o programa prar sortear um aluno que irá apagar o quadro")

#Coleta de dados
um = str(input("Qual o nome do primeiro aluno? "))
dois = str(input("Qual o nome do segundo aluno? "))
tres = str(input("Qual o nome do terceiro aluno? "))
quatro = str(input("Qual o nome do quarto aluno? "))

#Usando o Random Choice para sortear
sorteio = random.choice([um, dois, tres, quatro])

#Resultado
print(f"O aluno que irá apagar o quadro será {sorteio}")
