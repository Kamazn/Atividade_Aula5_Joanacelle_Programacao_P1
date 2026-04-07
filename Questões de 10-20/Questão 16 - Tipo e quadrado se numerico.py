# Questão 16 - Leia um valor e: Mostre o tipo; Se for numérico (após conversão) → mostre o quadrado
valor = input("Questão 16 - Digite um valor (Se for numérico, mostrará o quadrado): ")  # Recebe o valor do usuário como string

if valor.isdigit():      
    valor = int(valor)
    print("Tipo:", type(valor).__name__, "Valor:", valor ** 2)
else:
    print("Tipo:", type(valor).__name__,"Não é numerico")
    
    '''isdigit() serve para descobrir se o que o usuário escreveu é númerico'''