# Exercício Python 30: Crie um programa que leia um número
# inteiro e mostre na tela se ele é PAR ou ÍMPAR.
from time import sleep
numero = int(input('Digite um número : '))
print(f'PROCESSANDO')
sleep(3)
print(F'Analisando o número {numero}')

if numero % 2 == 0 :
    print('O número é PAR')
else:
    print('o número é IMPAR')