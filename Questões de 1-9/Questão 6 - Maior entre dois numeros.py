# Questão 6 - Leia dois números e exiba qual é o maior
print("Questão 6 - Digite dois número para saber qual o maior") 
numero1 = float(input("Digite o primeiro número: ")) # Recebe o primeiro número do usuário 
numero2 = float(input("Digite o segundo número: ")) # Recebe o segundo número do usuário 

if (numero1 == numero2): # Se o numero1 for igual ao numero2 
    print("Iguais") # Será iguais
else: # Se não for
    if (numero1 > numero2): # Se o numero1 foi maior que numero2
        print("Maior numero:", numero1) # Será o numero 1
    else: # Se não for
        print("Maior numero:", numero2) # Será o numero 2