# Exercício Python 14: Escreva um programa que converta uma 
#temperatura digitando em graus Celsius e converta para graus Fahrenheit.
tempeC  = float(input(' Qual é a temperatura em graus celcius C° '))
temF = ((tempeC * 9)/5) + 32
print(f''' A temperatura de C° {tempeC:.1f} graus
 Convertida para Fahrenhheit è de F° {temF:.1f} graus''')