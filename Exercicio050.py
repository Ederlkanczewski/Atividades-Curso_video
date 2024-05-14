soma = 0
contador = 0
for num in range (1,7):
    num = int(input(f'Digite {num} valor: '))
    if num % 2 == 0:
       contador = contador + 1
       soma = soma + num
print(f'Você digitou {contador} números PARES e a soma é {soma}')


    

