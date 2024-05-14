peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (M) '))
print(f'''Seu peso: {peso}  
E sua altura: {altura}''')
imc = peso / (altura** 2)
print(f'Seu IMC: {imc:.2f}')
if imc <= 18.5:
    print('Você está ABAIXO DO PESO!')
elif 18.5 <= 25:
    print('Você está no peso IDEAL!')
elif 25 <= 30:
    print('Cuidado você está com SOBREPESO! ')
elif 30 <= 40:
    print('Alerta você está com OBESIDADE!')
else:
    print('ALERTA você está com OBESIDADE MÓRBIDA!')









