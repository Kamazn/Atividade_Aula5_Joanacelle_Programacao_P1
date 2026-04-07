# Questão 17 - Leia idade e: Mostre: Menor de idade (<18); Adulto (18 a 59); Idoso (60+)
numero = int(input("Questão 17 - Digite sua idade: ")) # Recebe o número inteiro do usuário 

if (numero < 18): # Se o numero for menor que 18
    print("Menor de idade") # Será Menor de idade
else: # Se não for
    if (numero >= 18) and (numero <= 59): # Se o numero foi maior que 18 e menor que 59
        print("Adulto") # Será adulto
    else: # Se não for
        print("Idoso") # Será idoso