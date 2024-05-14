# Exercício Python 006: 
# Crie um algoritmo que leia um número e 
# mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um numero : '))
d = n * 2
t = n * 3
r = n ** (1/2)
print(f' O dobro de {n} é {d}\n O triplo é {t}\n Raiz quadrda é {r:.2f}')