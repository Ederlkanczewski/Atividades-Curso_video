#Exercício Python 7:
# Desenvolva um programa que leia as duas notas de um aluno, 
# calcule e mostre a sua média.
nota1 = float(input('Nota 1 : '))
nota2 = float(input('Nota 2 : '))
nota_final = (nota1 + nota2) / 2
print(f' A media final é {nota_final:.1f}')
