soma = 0
contador = 0
for numeros in range(1,501,2):
    if numeros % 3 == 0:
        contador = contador + 1
        soma = soma + numeros    
print(f'A somas dos {contador} mutlipos de 3 é {soma}')
