#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

#– O nome com todas as letras maiúsculas e minúsculas.

#– Quantas letras ao todo (sem considerar espaços).

#– Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo : ')).strip()
nome = nome.lower()
nome1 = nome.upper()
nome2 = len(nome) -nome.count(' ')
nome3 = nome.find(' ')
separa = nome.split ()
separa = separa[0]
separa2 =len(separa)
separa3 = separa.capitalize()

print(f'Seu primeiro nome é {separa3} e tem {separa2} letras')
print(F'''Seu nome minusculo {nome}
Seu nome maisculo {nome1}
Seu nome tem {nome2} letras
Seu primeiro nome tem {nome3} letras''')