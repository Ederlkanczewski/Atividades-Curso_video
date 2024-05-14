# Exercício Python 37: Escreva um programa em Python que leia 
# um número inteiro qualquer e peça para o usuário escolher 
# qual será a base de conversão: 
# 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um número: '))
print('1-> Binario, 2-> Octal, 3-> Hexadecimal')
opcao = int(input('Digite a opção desejada: '))

if opcao == 1:
 print('Você escloheu opção Binária!!')
 numero = bin(numero)
 print(f'O número escolhido em binário é: {numero[2:]}')
  
elif opcao == 2:
 print('Você escloheu opção Octadecimal!!')
 numero = oct(numero)
 print(f'O número escolhido em octadecimal é: {numero[2:]}')
  
elif opcao == 3:
 print('Você escloheu opção Hexadecimal!!')
 numero = hex(numero)
 print(f'O número escolhido em hexadecimal {numero[2:]}')
   