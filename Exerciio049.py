tabuada = 0
n = int(input('Digite um número: '))
for num in range(0,11):
    tabuada = num * n
    print(f'{n} X {num} = {tabuada}')
