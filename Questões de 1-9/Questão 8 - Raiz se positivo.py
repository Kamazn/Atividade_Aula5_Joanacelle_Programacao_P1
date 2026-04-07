# Questão 8 - Leia um número e: Se for positivo, mostre a raiz aproximada (use **0.5); Caso contrário, informe “Número inválido”
numero = float(input("Questão 8 - Digite um número positivo para saber a raiz aproximada: ")) # Recebe o número do usuário 

if numero > 0:
    print("A raiz quadrada aproximada do seu número é:",numero ** 0.5)
else:
    print("Número inválido, digite outro.")