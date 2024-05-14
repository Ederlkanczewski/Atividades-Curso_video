# Exercício Python 18: 
#Faça um programa que leia um ângulo qualquer e mostre na tela 
#o valor do seno, cosseno e tangente desse ângulo
import math
angulo = float(input('Digite o angulo : '))
math.radians
sen = math.sin(math.radians(angulo))
print(f'O angulo de {angulo} tem o SENO de {sen:.2f}')
cos = math.cos(math.radians(angulo))
print(f'O angulo de {angulo} tem o COSSENO de {cos:.2f}')
tang = math.tan(math.radians(angulo))
print(f'O angulo de {angulo} tem a TANGENTE de {tang:.2f}')