from math import radians,sin,cos,tan
angulo = float(input('Digite o angulo : '))
sen = sin(radians(angulo))
print(f'O angulo de {angulo} tem o SENO de {sen:.2f}')
coss = cos(radians(angulo))
print(f'O angulo de {angulo} tem o COSSENO de {coss:.2f}')
tang = tan(radians(angulo))
print(f'O angulo de {angulo} tem o TANGENTE de {tang:.2f}')
