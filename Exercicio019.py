#Exercício Python 19: Um professor quer sortear 
#um dos seus quatro alunos para apagar o quadro. 
#Faça um programa que ajude ele, lendo o 
#nome dos alunos e escrevendo na tela o nome do escolhido.
import random
aluno1 = str(input('Primeiro aluno : '))
aluno2 = str(input('Segundo aluno  : '))
aluno3 = str(input('Terceiro aluno : '))
aluno4 = str(input('Quarto aluno   : '))
aluno5 = str(input('Quinto aluno   : '))

nomes = [aluno1,aluno2,aluno3,aluno4,aluno5]

esolhido = random.choice(nomes)

print(f'O aluno escolido foi {esolhido} !!!')
