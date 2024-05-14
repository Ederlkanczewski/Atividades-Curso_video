# Exercício Python 13: Faça um algoritmo que leia o salário 
#de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Qual seu salario R$ '))
aumento = salario + (salario * 15 / 100)
print(f'Seu salario com aumento de 15% é R$ {aumento:.2f} reais : ')
