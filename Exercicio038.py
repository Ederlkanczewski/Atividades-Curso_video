#Exercício Python 038: Escreva um programa que leia 
#dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais


valor_1 = int(input('Digite o primeiro valor: '))
valor_2 = int(input('Digite o segundo valor: '))

if valor_1 > valor_2:
    print(f'O {valor_1} é maior que o {valor_2}')

elif valor_2 > valor_1:
     print(f'O {valor_2} é maior que o {valor_1}')

else:
     print('Não existe valor maior,os dois são iguais.')

