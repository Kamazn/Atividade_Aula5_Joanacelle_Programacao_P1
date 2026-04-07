# Questão 19 - Leia dois números e: Verifique se são iguais ou diferentes. Sendo diferentes mostre a diferença entre eles
print("Questão 19 - Digite dois números e verifique se são iguais ou diferentes")
numero1 = float(input("Digite o primeiro número: ")) # Recebe o primeiro número
numero2 = float(input("Digite o segundo número: ")) # Recebe o segundo número

if numero1 == numero2: # Se forem iguais
    print("Os números são iguais") # Mostra que são iguais
else: # Se forem diferentes
    diferenca = (numero1 - numero2) # Calcula a diferença 
    print("Os números são diferentes. Diferença:", diferenca) # Mostra a diferença