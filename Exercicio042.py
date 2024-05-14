print('-=-'*20)
print('ANALISADOR DE TRIÂNGULO')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 : # CÁLCULO PARA FORMAR TRIANGULO
    print('os segmentos acima PODEM FORMAR UM TRIÂNGULO !')
    if r1 == r2 == r3:
        print("Triângulo Equilatero")
    if (r1 == r2 and r3 != r1) or (r1 == r3 and r2 != r1) or (r2 == r3 and r2 != r1):
        print('Triâgulo Isólsceles')
    if r1 != r2 != r3 !=r1 :
        print('Triângulo Escaleno')
else:
    print(f'Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO !')
    