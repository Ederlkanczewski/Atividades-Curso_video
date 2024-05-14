while True:
 print('Digite a opção desejada!')
 print('1-> Cadastrar atleta, 2-> Finalizar ')
 opcao = int(input('Digite a opção desejada: '))
 if opcao == 1:
    print('1-> Cadastrar atleta')
    nasc = int(input('Ano de nascimento: '))
    from datetime import date
    atual = date.today().year
    idade = atual - nasc
    print(f'O atleta tem {idade} anos' )
    if idade <= 9:
        print('categoria MIRIN ')
    elif idade <= 14:
        print('Categoria INFANTIL')
    elif idade <= 19:
        print('Categoria JÚNIOR')
    elif idade <= 25:
        print('Categoria SENIOR')
    else:
        print('Categoria MASTER'),
 elif opcao == 2:
  print('2-> Finalizar')
 else:
    print('Opção Inválida!')
 break



