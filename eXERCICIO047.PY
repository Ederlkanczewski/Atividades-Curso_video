from time import sleep
for numeros in range(1, 51):
    if numeros % 2 == 0:
        print(numeros, end=' ')
        sleep(1)
print('ACABOU')
