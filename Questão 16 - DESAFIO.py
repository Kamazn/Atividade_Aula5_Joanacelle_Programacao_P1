# Questão 16 - Leia um valor e: Mostre o tipo; Se for numérico (após conversão) → mostre o quadrado
valor = input("Questão 16 - Digite um valor (Se for numérico, mostrará o quadrado): ")  # Recebe o valor do usuário como string

if valor >= "0" and valor <= "99999999": # Se o valor for igual ou maior que zero e igual ou menor que 9999999
    valor = float(valor) # Ele converte para float 
    print("Tipe:", type(valor), "Valor:", valor ** 2) # Mostra o tipo + o quadrado
else: # Se não for
        if valor < "0": # Se o valor for menor que 0
              valor = float(valor) # Ele converte para float 
              print("Tipe:", type(valor), "Numero negativo não tem raiz") # Mostra que numero negativo nao tem raiz, pra evitar do numero negativo sair como str
        else: # Se não for
              valor = str(valor) # Converte para str
              print("Tipo:", type(valor), "Valor não é numerico") # Mostra o tipo e que não é númerico
