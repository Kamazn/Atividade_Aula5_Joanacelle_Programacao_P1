# Questão 12 - Leia dois números e: Mostre a soma; Mostre qual é maior ou se são iguais.
print("Questão 12 - Digite dois número para saber a soma, qual é maior ou se são iguais") 
numero1 = float(input("Digite o primeiro número: ")) # Recebe o primeiro número do usuário 
numero2 = float(input("Digite o segundo número: ")) # Recebe o segundo número do usuário 

print("Resultado da soma:", numero1 + numero2)

if (numero1 == numero2): # Se o numero1 for igual ao numero2 
    print("Iguais") # Será iguais
else: # Se não for
    if (numero1 > numero2): # Se o numero1 foi maior que numero2
        print("Maior numero:", numero1) # Será o numero 1
    else: # Se não for
        print("Maior numero:", numero2) # Será o numero 2