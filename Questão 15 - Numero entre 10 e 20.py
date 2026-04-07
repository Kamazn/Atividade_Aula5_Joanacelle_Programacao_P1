# Questão 15 - Leia um número e: Se estiver entre 10 e 20 → “Dentro”; Caso contrário → “Fora”
numero = float(input("Questão 15 - Digite um número para saber se está entre 10 e 20: ")) # Recebe o número do usuário 

if (numero >= 10) and (numero <= 20): # Verifica se o numero fica entre 10 e 20
               print("Dentro") # Fica entre 10 e 20
else: # Se não for 
               print("Fora") # Não fica entre 10 e 20
