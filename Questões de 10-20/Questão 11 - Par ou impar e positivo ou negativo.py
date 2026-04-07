# Questão 11 - Leia um número e: Se for par e positivo → “Par positivo”; Se for par e negativo → “Par negativo”; Caso contrário → “Ímpar”
numero = int(input("Questão 11 - Digite um número para saber se é par positivo/negativo ou ímpar: ")) # Recebe o número inteiro do usario

if (numero % 2 == 0): # Verifica se o numero é positivo
        if (numero > 0):
               print("Par positivo") # Será par positivo
        else: # Se não for 
               print("Par negativo") # Será par negativo
else:
     print("Ímpar") # Será Ímpar