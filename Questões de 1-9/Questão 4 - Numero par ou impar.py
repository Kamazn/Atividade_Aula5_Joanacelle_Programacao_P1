# Questão 4 - Leia um número e informe se ele é par ou ímpar.
numero = float(input("Questão 4 - Digite um número para saber se é par ou impar: ")) # Recebe o número inteiro do usuário 

if (numero == 0): # Se o numero for igual a 0
    print("Zero") # Será zero
else: # Se não for
    if (numero % 2 == 0): # Verifica se o numero é par
        print("Par") # Será positivo 
    else: # Se não for
        print("Ímpar") # Será negativo