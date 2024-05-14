# Entrada do usuário
numero = int(input("Digite um número inteiro: "))

# Verificação se é primo ou não
if numero < 2:
    print(f"{numero} não é um número primo.")
else:
    primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            primo = False
            break

    if primo:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")
