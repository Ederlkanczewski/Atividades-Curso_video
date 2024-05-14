#Exercício Python 17: 
#Faça um programa que leia o comprimento do cateto oposto e 
#do cateto adjacente de um triângulo retângulo. 
#Calcule e mostre o comprimento da hipotenusa.
cadjacente = float(input('Qual é o valor do Cateto adjacente : '))
coposto = float(input('Qual o valor do cateto oposto : '))
hipotenusa = (cadjacente * cadjacente + coposto * coposto)** 0.5
print(f' O valor da hipotenusa é : {hipotenusa:.2f}')