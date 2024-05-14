# Exercício Python 10: Crie um programa que leia
# quanto dinheiro uma pessoa tem na carteira e 
# mostre quantos dólares ela pode comprar.
R = float(input('quantos reais R$ : '))
Dolar_americano = R / 4.98 
Euro = R / 5.29
Iene = R / 0.034
Libra_estrelina = R / 6.16
Franco_suiço = R / 5.53
Dolar_canadense = R / 3.63
Dolar_australiano = R / 3.17
Yuan = R / 0.68
Rand = R / 0.26
Peso_argentino = R / 0.014

print(f''' Você pode compra US$ {Dolar_americano:.2f} Dolars !\n
      Você pode compra EUR $ {Euro:.2f} Euros !\n 
      Você pode compra JPY$ {Iene:.2f} Iene !\n
      Você pode compra GBP$ {Libra_estrelina:.2f} Libras Estrilas !\n 
      Você pode compra CHF$ {Franco_suiço:.2f} Franco Suiço !\n
      Você pode compra CAD$ {Dolar_canadense:.2f} Dolar Canadense !\n
      Você pode compra AUD$ {Dolar_australiano:.2f} Dolar Australiano !\n
      Você pode compra CNY$ {Yuan:.2f} Yuan !\n
      Você pode compra ZAR$ {Rand:.2f} Rand !\n
      Você pode compra ARS$ {Peso_argentino:.2f} Peso Argentino ! '''
      )