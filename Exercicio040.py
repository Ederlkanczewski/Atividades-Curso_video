#Exercício Python 040: Crie um programa que leia duas notas 
#de um aluno e calcule sua média, 
#mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO
while True:
 print('Digite a opção desejada!')
 print('1-> Caucular média, 2-> Finalizar ')
 opcao = int(input('Digite a opção desejada: '))
 if opcao == 1:
    print('1-> Caucular média')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2)/2
    print(f'''Sua primeira nota foi {nota1}
Sua segunda nota foi {nota2} 
A média é: {media:.1f}''')

    if media  >= 7.0 and media <=10:
        print(f'Parabéns você foi aprovado!!!')

    elif media >= 5.0 and media < 7.0 :
        print(f'Voê está de recuperação!!!')
    elif media >= 0 and  media < 5.0:
        print(f'Você está reprovado!!!')
    else:
        print(f'Operação inválida!!!')
 elif opcao == 2:
  print('2-> Finalizar')
 else:
    print('Opção Inválida!')
 break