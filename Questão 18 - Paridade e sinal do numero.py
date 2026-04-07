# Questão 18 - Leia um número e: Mostre se ele é par positivo, par negativo, impar positivo, impar negativo ou neutro
numero = int(input("Questão 18 - Digite um número para saber se é par positivo/negativo, ímpar positivo/negativo ou neutro: ")) # Recebe o número inteiro do usuário 

if numero == 0: # Se o número for 0
    print("Neutro") # É neutro
elif numero > 0: # Se for maior que 0
    if numero % 2 == 0: # Verifica se é par
        print("Par positivo") # Par positivo
    else: # Se não for par
        print("Ímpar positivo") # Ímpar positivo
else: # Se for menor que 0
    if numero % 2 == 0: # Verifica se é par
        print("Par negativo") # Par e negativo
    else: # Se não for par
        print("Ímpar negativo") # Ímpar e negativo