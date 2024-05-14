# Exercício Python 12: Faça um algoritmo que leia o preço 
#de um produto e mostre seu novo preço, com 5% de desconto.
produto = float(input('Qual valor do produto R$ '))
desconto = produto - (produto*5/100)

print(f'''O valor do produto è {produto}
Na promoção com 5% de desconto vai custar R$ {desconto:.2f}. ''')