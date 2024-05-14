# Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade  = float(input('Qual é velocidade  do carro : '))
if velocidade < 80:
    print(f'''Sua velocidade foi {velocidade:.2f}
OK está dentro do limite
Boa Viagem!''') 
else:
    print(f'''Sua velocidade foi {velocidade:.2f}
Acima do limite que é de 80.00 km/h 
Você foi multado!''')
    multa = (velocidade - 80.00)* 7.00
    print(f'Valor da multa é R$ {multa:.2f} reais')
print(f'Tenha um bom dia dirija com segurça!')
