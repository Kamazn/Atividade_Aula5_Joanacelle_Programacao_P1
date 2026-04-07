# Questão 3 - Leia um valor e: Mostre o valor digitado; Mostre o tipo da variável usando type()
valor = input("Questão 3 - Digite um valor para saber o tipo da variavel: ")  # Recebe o valor do usuario como string

'''isdigit() serve para descobrir se oque pessoa escreveu é númerico '''

if valor.isdigit(): # Verifica se o valor é um numero
    valor = int(valor) # Converte o valor para inteiro
    print("Valor digitado:", valor, "Tipo:", type(valor).__name__) # Mostra o valor dele e o tipo como inteiro
else:
    print("Valor digitado:", valor, "Tipo:", type(valor).__name__) # Mostra o valorde ele e o tipo como string

    '''".__name__" é para mostrar apenas o tipo, sem o "type"'''