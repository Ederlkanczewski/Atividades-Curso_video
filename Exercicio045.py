from random import randint
from time import sleep
jogadas = ('\033[32m1-> pedra,2-> papel,3-> tesoura')
pc = randint(0,2)
print('''\033[34mJOGADAS 
1-> pedra,
2-> papel,
3-> tesoura ''')
jogador = int(input('\033[32mQUAL É SUA JOGADA: '))
print('\033[1;33mJO')
sleep(1)
print('\033[1;33mKEN')
sleep(1)
print('\033[1;33mPO')
print('\033[31m=>'*11)
print(f'PC JOGOU: {pc}')
print(f'JOGADOR JOGOU: {jogador}')
print('\033[31m=>'*11)
if pc == 1 :
    if jogador == 1:
        print('\033[33mPC EMPATE!!!')
    elif jogador == 2:
        print('\033[32mJOGADOR VENCE!!!')
    elif jogador == 3:
        print('\033[32mPC VENCE!!!')
    else:
        print('JOGADA INVÁLIDA!!!')
elif pc == 2:
    if jogador == 1:
        print('\033[32mPC VENCE!!!')
    elif jogador == 2:
        print('\033[33mPC EMPATE!!!')
    elif jogador == 3:
        print('\033[32mJOGADOR VENCE!!!')
    else:
        print('JOGADA INVÁLIDA!!!')
elif pc == 3:
    if jogador == 1:
        print('\033[32mJOGADOR VENCE!!!')
    elif jogador == 2:
        print('\033[32mPC VENCE!!!')
    elif jogador == 3:
        print('\033[33mPC EMPATE!!!')
    else:
        print('JOGADA INVÁLIDA!!!')


 
    
    

