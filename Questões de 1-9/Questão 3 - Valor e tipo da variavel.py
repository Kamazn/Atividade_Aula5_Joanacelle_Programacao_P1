# Questão 3 - Leia um valor e: Mostre o valor digitado; Mostre o tipo da variável usando type()
valor = input("Questão 3 - Digite um valor para saber o tipo da variavel: ")  # Recebe o valor do usuario como string

if valor.isdigit(): # Verifica se é inteiro
    valor_convertido = int(valor) # Converte para inteiro
elif valor.replace('.', '', 1).replace('-', '', 1).isdigit():  # Verifica se é float 
    valor_convertido = float(valor) # Converte para float
elif valor.lower() == "true" or valor.lower() == "false":  # Verifica se é booleano
    valor_convertido = valor.lower() == "true" # Converte para bool
else:
    valor_convertido = valor  # se não for nenhum dos acima, deixa como string

print("Valor digitado:", valor_convertido, "Tipo:", type(valor_convertido).__name__) # Mostra o valor, e o tipo dele, ".__name__" é para mostrar apenas o tipo, sem o "type"
