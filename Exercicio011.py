# Exercício Python 11:
# Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados
L = float(input('Digite o largura : '))
A = float(input('Digite o altura : '))
AR = L * A
print(f'Sua parde tem {L} X {A} um total de {AR} quadrados.')
T = AR / 2
print(f'Voê pricisa de : {T:.2f} litros.')
