#Exercício Python 15: Escreva um programa que pergunte 
# a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado
dia = int(input( 'Quantidade de dias com o carro : '))
km_rodado = float(input( 'Quantos km percorrido : '))

total = (dia * 60) + (km_rodado * 0.15)
print(f'Total dia com carro {dia}\nTotal de km rodado {km_rodado}\nTotal a pagar é R$ {total:.2f}')
