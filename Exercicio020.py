#Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação
# de trabalhos dos alunos. Faça um programa que leia o nome 
#dos quatro alunos e mostre a ordem sorteada.
import random

aluno1 = str(input('Primeiro aluno : '))
aluno2 = str(input('segundo aluno  : '))
aluno3 = str(input('terceiro aluno : '))
aluno4 = str(input('Quarto aluno   : '))

alunos = [aluno1, aluno2 , aluno3, aluno4]

ordem = random.shuffle(alunos)

print(f'A ordem dos aluno para a apresentação é : \n{alunos}')