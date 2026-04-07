# Questão 14 - Leia um valor e: Converta para inteiro; Se for múltiplo de 3 → “Múltiplo de 3”; Senão → “Não é múltiplo"
numero = input("Questão 14 - Digite um número para saber se é múltiplo de 3: ") # Recebe o número do usuario como string
numero = int(numero) # Converte para inteiro

if (numero % 3 == 0): # Se o numero for múltiplo de 3
    print("Múltiplo de 3") # Será múltiplo de 3
else: # Se não for
        print("Não é múltiplo") # Não será múltiplo de 3