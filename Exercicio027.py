# Exercício Python 27: Faça um programa que leia o nome completo
# de uma pessoa, mostrando em seguida o primeiro 
# e o último nome separadamente.
nome = str(input(' Digite seu nome completo: ')).strip()
nome1 = (nome.split()[0])
nome2 = (nome.split()[-1])
print(f'''Muito prazer em te conhcer !
Seu primeiro nemo é : {nome1}
Seu último nome é   : {nome2}''')  