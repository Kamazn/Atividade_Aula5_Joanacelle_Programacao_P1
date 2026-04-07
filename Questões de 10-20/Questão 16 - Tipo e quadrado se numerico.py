# Questão 16 - Leia um valor e: Mostre o tipo; Se for numérico (após conversão) → mostre o quadrado
valor = input("Questão 16 - Digite um valor (Se for numérico, mostrará o quadrado): ")  # Recebe o valor do usuário como string

if valor.isdigit(): # Verifica se é inteiro
    valor_convertido = int(valor) # Converte para inteiro
elif valor.replace('.', '', 1).isdigit(): # verifica se é float
    valor_convertido = float(valor) # Converte para float
else:
    valor_convertido = valor  # se não for número, deixa como string

if isinstance(valor_convertido, (int, float)): # isinstance serve pra verificar se o tipo é int ou float
    print("Tipo:", type(valor_convertido).__name__, "Quadrado:", valor_convertido ** 2) # Se for, mostra o quadrado
else:
    print("Tipo:", type(valor_convertido).__name__, "Não é numérico, não tem quadrado") # Se não for, não mostra