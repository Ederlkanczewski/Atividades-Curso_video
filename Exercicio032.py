# Exercício Python 32: Faça um programa que 
# leia um ano qualquer e mostre se ele é bissex
from datetime import date
ano = int(input('Que ano vamos analizar ano ? Coloque 0 para analizar o ano atual : '))
if ano == 0 :
 ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano  % 400 ==  0 :
    print(f'O ano {ano} é BISSEXTO') 
else:
    print(f'O ano {ano} não BISSEXTO')  

