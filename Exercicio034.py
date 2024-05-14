# Exercício Python 34: Escreva um programa que pergunte o salário 
# de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Informe seu sálario? R$ '))
print(f'O salário informado é R$ {salario}')

if salario > 1250 :
    aumento = salario + (salario*10/100)
else: 
    aumento = salario + (salario*15/100)

print(f'Seu novo salário é R$ {aumento:.2f}')