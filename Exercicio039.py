#Exercício Python 39: Faça um programa que leia 
#o ano de nascimento de um jovem e informe, 
#de acordo com a sua idade, 
#se ele ainda vai se alistar ao serviço militar, 
#se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} em {atual}')
if idade == 18:
    print('Você tem que se alistar!!')

elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para você se alistar!!')
    ano = atual + saldo
    print(f'Seu alistamnto será em {ano}')

elif idade > 18:
    saldo = idade - 18
    print(f'Você de veria ter se alistado ha {saldo} anos')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}')



