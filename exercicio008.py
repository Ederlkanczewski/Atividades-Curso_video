# Exercício Python 8: Escreva um programa que leia 
#um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('Digite um valor : '))
cm = m * 100
mm = m * 1000
print(f' {m} metros convertido em centimetros é {cm:.0f}\n {m} metros convertido em milimetros é {mm:.0f}')
