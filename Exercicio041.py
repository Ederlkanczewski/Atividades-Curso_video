
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'O atleta tem {idade} anos' )
if idade <= 9:
    print('categoria MIRIN ')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categorio JÚNIOR')
elif idade <= 25:
    print('Categoria SENIOR')
else:
    print('Categoria MASTER'),



