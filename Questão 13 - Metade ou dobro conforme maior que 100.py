# Questão 13 - Leia um número e: Se for maior que 100 → mostre metade; Senão → mostre o dobro.
numero = int(input("Questão 13 - Digite um número, acima de 100 mostra metade, abaixo de 100 mostra o dobro: ")) # Recebe o número do usuário 

if (numero > 100): # Se o numero for maior que 100
    print("Resultado: ", numero / 2) # Será metade
else: # Se não for
        print("Resultado:", numero * 2) # Será o dobro