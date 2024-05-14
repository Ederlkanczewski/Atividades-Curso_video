frase = str(input('Digite sua frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto)-1 , -1 ,-1):
    inverso += junto[letra]
print(f'O inverso {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndomo!!')
else:
    print('A frase digitada não é um palíndromo!')

