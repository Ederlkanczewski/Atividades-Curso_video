frase = 'Curso em Video'
print(frase[3]) # terceiro caracter
print(frase[3:13])# terceiro carcter até o caracter 13
print(frase[:13]) # do inicio da string até o 13 carcter
print(frase[13:]) # do 13 carcter até o final da string
print(frase[1:15]) # do 1 carcter até o  15 carcter
print(frase[1:15:2]) # do 1 carcter até o 15 carcter pulando de  2 em 2
print(frase[1::2]) # do 1 carcter ate o final da string pulando de 2 em 2
print(frase[::2]) # do inicio da string ste o final pulando de 2 em 2
print(frase[1:15]) # do 1 carcter até o 15 carcter 
print(frase.count('o')) # contar quantas vezes aparece a palavra 'o' minuscula na string 
print(frase.upper().count('o')) # contar quantas vezes aparece a palavra 'o' maiuscula na str
print(len(frase)) # pra saber o tamanho da string com espaços
print(len(frase.strip())) #ignora os espaços
print(frase.replace('Python','Android')) # substitui a palavra python por android na string

print('Curso' in frase) # mostrar que a palavra está na frase
print(frase.find('Curso')) #mostra a posição que a palvra está na string
print(frase.lower().find('Curso')) # existe a palavra transformado em minusculo
print(frase.split('Curso')) # cria uma lista  da frase
 
