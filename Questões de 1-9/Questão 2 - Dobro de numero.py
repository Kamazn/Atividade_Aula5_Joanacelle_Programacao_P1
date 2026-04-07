# Questão 2 - Leia um número (entrada padrão do input) e: Converta para inteiro; Exiba o dobro do valor.
numero = (input("Questão 2 - Digite um número inteiro para calcular o dobro: ")) # Recebe o número do usuario como string
numero = int(numero) # Converte para int

resultado = numero * 2 # Calcula o dobro do número
print("Resultado:", resultado, "Tipo:", type(numero).__name__) # Mostra o resultado e o tipo da variável