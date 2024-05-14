#'''case Exercício Python 26 Faça um programa que leia uma frase 
#pelo teclado e mostre quantas vezes aparece a letra “A”
#em que posição ela aparece a primeira vez e em que posição ela aparece a'''

frase = str(input('Digite uma frase : ')).upper().strip()
frase1 = frase.count('A')
frase2 =(frase.find('A')+1)
frase3 = (frase.rfind('A')+1)
print(f'''A letra A apareceu {frase1} vezes na frase.
A primera letra A apareceu na posição {frase2}
A últimaletra A apareceu na posição {frase3}''')