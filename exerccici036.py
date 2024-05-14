# Exercício Python 36: Escreva um programa para aprovar o 
# empréstimo bancário para a compra de uma casa. Pergunte o 
# valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 
# 30% do salário ou então o empréstimo será negado.

casa = float(input('Digite o valor da casa : '))
salario = float(input('Qual é seu salário : R$ '))
anos = int(input('Quantos anos de contrato : '))
prestacao = casa / (anos * 12)
minimo = (salario * 30) / 100
print(F'Para pagar uma casa no valor de R$ {casa:.2f} em {anos}')
print(f'A prestação séra de R$ {prestacao:.2f}')

if prestacao <= minimo:
   print(f'EmprÉstimo CONCEDIDO!!!')
 
else:
   print(f'Empréstimo NEGADO !!!')


  


