nome = str(input('Qual é o seu nome ?  '))
if nome == 'Gustavo' :
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo' :
    print('Seu nome é bem populare no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome femenino')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia {nome} !!!')