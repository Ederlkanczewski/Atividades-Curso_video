# Exercício Python 28: Escreva um programa que faça
# o computador “pensar” em um número inteiro entre 0 e 5 e peça para
# o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint # Biblioteca que faz escolher um número aleatório
from time import sleep # Biblioteca para contagem de tempo

computador = randint(0,5) # FAZ O COMPUTADOR ESCOLHER UM NUMERO ALEATÓRIO ENTRE AS OPÇÕES QUE ESTÃO ENTRE PARENTES
print('-=-'*20)
print(f'Pensei em número você sabe qual é ?') # JOGADOR ESCOLHE O NÚMERO
print('-=-'*20)
jogador  = int(input('digite um numero : '))
print(f'PROCESSANDO')
sleep(3) # Espera o tempo entre parentes 



if jogador == computador :
    print('Você acertou PRABÉNS!')
else:
    print(f'Você erro eu pensei no numero {computador} TENTE DE NOVO!')