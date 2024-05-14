primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10-1) * razao
for num in range (primeiro,11,razao):
 print(f'{num}' ,end= '->')
print('ACABOU')
