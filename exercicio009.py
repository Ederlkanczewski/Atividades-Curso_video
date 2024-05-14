# Exercício Python 9: Faça um programa que leia 
#um número Inteiro qualquer e mostre na tela a sua tabuada
n = int(input('Digite um numero : '))
print('=' * 12)
n1 = 1 
while n1 <= 10:
    print(n1 , 'x', n, '=', n  * n1 )
    n1 = n1 + 1
print('=' * 12)