# Questão 10 - Leia um número e informe: “Dentro do intervalo” se estiver entre 0 e 10; “Fora do intervalo” caso contrário
numero = float(input("Questão 10 - Digite um número para saber se está entre 0 e 10: ")) # Recebe o número do usuário 

if (numero >= 0): # Verifica se o numero fica entre 0 e 10
        if (numero <= 10):
               print("Dentro do intervalo") # Fica entre 0 e 10
        else: # Se não for 
               print("Fora do intervalo") # Não fica entre 0 e 10
else:
     print("Fora do intervalo") # Não fica entre 0 e 10