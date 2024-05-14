# Exercício Python 31: Desenvolva um programa que pergunte
# a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50
# por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

from time import sleep
distancia = float(input('Qual distância percorrida : '))
print('PROCESSANDO')
sleep(3)
valor1 = distancia * 0.50
valor2 = distancia *0.45

if distancia <=200:
    print(f'Valor da viagem foi R$ {valor1:.2f}')
else:
    print(f'Valor da viagem foi R$ {valor2}')