print('='*20)
print('LOJÃO DO PYTHON')
print('='*20)
while True:
    print('FORMAS DE PAGAMENTO')
    print('''0-> Finalizar programa 
1-> Á vista dinheiro/cheque
2-> À vista cartão
3-> 2X no cartão
4-> 3X no cartão''')
    opcao = ('1 -> Á vista dinheiro/cheque,2-> À vista cartão, 3-> 2X no cartão, 4-> 3X no cartão  ')
    opcao = int(input('Qual é a opção: '))
    def menu ():
        if opcao ==  0:
            print('Progama finalizado!')
        elif opcao == 1 :
            print('Á vista dinheiro/cheque')
            a_vista = (produto * 10)/100 
            desc = produto - a_vista
            print(f'O preço final do seu produto é R$ {desc}')
        elif opcao == 2:
            print('À vista cartão')
            a_vst_cat = (produto * 5)/100 
            desco = produto - a_vst_cat
            print(f'O preço final do seu produto é R$ {desco}')
        elif opcao == 3 :
            print(f'2X no cartão')
            duas_x_cat = produto 
            preco = produto/2
            print(f'Sua compra em 2X será de R$ {preco:.2f}')
            print(f'O preço final do seu produto em 2X no cartão será de  R${produto:.2F}')
        elif opcao == 4:
            print('3X no cartão')
            tres_x_cat = (produto * 20)/100 
            juros = produto + tres_x_cat
            prefinal = juros / 3
            print(f'Sua compra em 2X será de R$ {prefinal:.2f}')
            print(f'O preço final do seu produto no cartão em 3X é R$ {juros:.2F} ')
        else:
            print('OPÇÃO INVÁLIDA!')
    menu()
    produto = float(input('Qual o valor do produto'))
    

   







