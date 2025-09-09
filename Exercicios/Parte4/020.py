#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos 4 alunos e mostre a ordem soteada
import random

print("Esse é o programa que irá sortear a ordem de apresentaçãoo dos trabalhos")
aluno1 = str(input("Qual o nome do primeiro aluno? "))
aluno2 = str(input("Qual o nome do segundo aluno? "))
aluno3 = str(input("Qual o nome do terceiro aluno? "))
aluno4 = str(input("Qual o nome do quarto aluno? "))

alunos = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(alunos)

print(f"A ordem de apresentação dos trabalhos será, respectivamente: {alunos}")
