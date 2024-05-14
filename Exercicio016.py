#Exercício Python 16: 
#Crie um programa que leia um número Real 
#qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
numero = float(input('Digite um numero : '))
print(f'O numero digitado foi {numero}\nE sua porção inteira é {trunc(numero)}')
