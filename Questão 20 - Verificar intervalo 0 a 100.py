# Questão 20 - Leia um valor e: verifique se eles está entre 0 e 100, caso o número esteja fora do intervalo, e mostre na tela o valor
valor = float(input("Questão 20 - Digite um valor, e veja se está entre 0 a 100: ")) # Recebe o valor do usuário

if 0 <= valor <= 100: # Se o valor estiver entre 0 e 100
    print("O valor está dentro do intervalo de 0 a 100") # Mostra que está dentro
else: # Se não for
    print("O valor está fora do intervalo:", valor) # Mostra que está fora