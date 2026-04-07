# ============================================================
# Atividade Aula 5 - Programação de Computadores - Joanacelle
# Teste de Mesa (10 Questões)
#============================================================

def questao1():
    # Verifica se o número é maior que 0 e menor que 5
    a = int(input("Questão 1 - Verifica se é maior que 0 e menor que 5: "))
    if a > 0:
        if a < 5:
            print("x")
        else:
            print("y")
    else:
        print("z")
    
    print("--- Fim da Questão 1 ---\n")
    
    # | Entrada | Saída | Explicação
    # |---------|-------|-------------------------------
    # | 2       | x     | 2>0 ✅ e 2<5 ✅ → imprime "x"
    # | 6       | y     | 6>0 ✅ e 6<5 ❌ → imprime "y"
    # | 0       | z     | 0>0 ❌ → cai no else → "z"
    # | -3      | z     | -3>0 ❌ → cai no else → "z"

def questao2():
    # Verifica se o número está entre 10 e 20
    a = int(input("Questão 2 - Verifica se está entre 10 e 20: "))
    if a >= 10:
        if a <= 20:
            print("a")
        else:
            print("b")
    else:
        print("c")
    
    print("--- Fim da Questão 2 ---\n")
    
    # | Entrada | Saída | Explicação
    # |---------|-------|-------------------------------
    # | 15      | a     | 15>=10 ✅ e 15<=20 ✅ → "a"
    # | 25      | b     | 25>=10 ✅ e 25<=20 ❌ → "b"
    # | 10      | a     | 10>=10 ✅ e 10<=20 ✅ → "a"
    # | 5       | c     | 5>=10 ❌ → cai no else → "c"

def questao3():
    # Diferencia positivo, negativo e zero
    a = int(input("Questão 3 - Verifica se é positivo, negativo ou zero: "))
    if a != 0:
        if a > 0:
            print("positivo")
        else:
            print("negativo")
    else:
        print("zero")
    
    print("--- Fim da Questão 3 ---\n")
    
    # | Entrada | Saída      | Explicação
    # |---------|------------|-------------------------------
    # | 5       | positivo   | 5!=0 ✅ e 5>0 ✅ → "positivo"
    # | -2      | negativo   | -2!=0 ✅ e -2>0 ❌ → "negativo"
    # | 0       | zero       | 0!=0 ❌ → "zero"
    # | 10      | positivo   | 10!=0 ✅ e 10>0 ✅ → "positivo"

def questao4():
    # Verifica se é par ou ímpar e se é maior que 10
    a = int(input("Questão 4 - Verifica se é par ou ímpar e se é maior que 10: "))
    if a % 2 == 0:
        if a > 10:
            print("A")
        else:
            print("B")
    else:
        print("C")
    
    print("--- Fim da Questão 4 ---\n")
    
    # | Entrada | Saída | Explicação
    # |---------|-------|-------------------------------
    # | 12      | A     | par ✅ e >10 ✅ → "A"
    # | 8       | B     | par ✅ e >10 ❌ → "B"
    # | 7       | C     | ímpar ❌ → "C"
    # | 11      | C     | ímpar ❌ → "C"

def questao5():
    # Verifica se é muito negativo, negativo ou positivo
    a = int(input("Questão 5 - Verifica se é muito negativo, negativo ou positivo: "))
    if a < 0:
        if a < -10:
            print("muito negativo")
        else:
            print("negativo")
    else:
        print("positivo")
    
    print("--- Fim da Questão 5 ---\n")
    
    # | Entrada | Saída           | Explicação
    # |---------|----------------|-------------------------------
    # | -15     | muito negativo | <0 ✅ e <-10 ✅ → "muito negativo"
    # | -5      | negativo       | <0 ✅ e <-10 ❌ → "negativo"
    # | 0       | positivo       | <0 ❌ → "positivo"
    # | 3       | positivo       | <0 ❌ → "positivo"

def questao6():
    # Verifica se está no intervalo entre 5 e 10, maior ou menor
    a = int(input("Questão 6 - Verifica intervalo entre 5 e 10, é maior ou menor: "))
    if a > 5:
        if a < 10:
            print("intervalo")
        else:
            print("maior")
    else:
        print("menor")
    
    print("--- Fim da Questão 6 ---\n")
    
    # | Entrada | Saída     | Explicação
    # |---------|-----------|-------------------------------
    # | 7       | intervalo | >5 ✅ e <10 ✅ → "intervalo"
    # | 12      | maior     | >5 ✅ e <10 ❌ → "maior"
    # | 5       | menor     | >5 ❌ → "menor"
    # | 3       | menor     | >5 ❌ → "menor"

def questao7():
    # Verifica se é zero, par ou ímpar
    a = int(input("Questão 7 - Verifica se é zero, par ou ímpar: "))
    if a == 0:
        print("zero")
    else:
        if a % 2 == 0:
            print("par")
        else:
            print("impar")
    
    print("--- Fim da Questão 7 ---\n")
    
    # | Entrada | Saída  | Explicação
    # |---------|--------|-------------------------------
    # | 0       | zero   | a==0 ✅ → "zero"
    # | 4       | par    | a==0 ❌, 4 é par → "par"
    # | 7       | impar  | a==0 ❌, 7 é impar → "impar"
    # | -3      | impar  | a==0 ❌, -3 é impar → "impar"

def questao8():
    # Verifica se o valor é alto, médio ou baixo
    a = int(input("Questão 8 - Verifica se é alto, médio ou baixo: "))
    if a > 100:
        print("alto")
    else:
        if a > 50:
            print("medio")
        else:
            print("baixo")
    
    print("--- Fim da Questão 8 ---\n")
    
    # | Entrada | Saída  | Explicação
    # |---------|--------|-------------------------------
    # | 120     | alto   | >100 ✅ → "alto"
    # | 70      | medio  | >100 ❌, >50 ✅ → "medio"
    # | 40      | baixo  | >100 ❌, >50 ❌ → "baixo"
    # | 50      | baixo  | >100 ❌, >50 ❌ → "baixo"

def questao9():
    # Diferencia nulo, positivo e negativo
    a = int(input("Questão 9 - Verifica se é nulo, positivo ou negativo: "))
    if a >= 0:
        if a == 0:
            print("nulo")
        else:
            print("positivo")
    else:
        print("negativo")
    
    print("--- Fim da Questão 9 ---\n")
    
    # | Entrada | Saída      | Explicação
    # |---------|------------|-------------------------------
    # | 0       | nulo       | >=0 ✅ e ==0 ✅ → "nulo"
    # | 5       | positivo   | >=0 ✅ e ==0 ❌ → "positivo"
    # | -2      | negativo   | >=0 ❌ → "negativo"
    # | 10      | positivo   | >=0 ✅ e ==0 ❌ → "positivo"

def questao10():
    # Verifica se é múltiplo de 3, não múltiplo ou negativo/zero
    a = int(input("Questão 10 - Verifica se é múltiplo de 3 ou não, ou negativo/zero: "))
    if a > 0:
        if a % 3 == 0:
            print("multiplo de 3")
        else:
            print("par nao multiplo")
    else:
        print("negativo ou zero")
    
    print("--- Fim da Questão 10 ---\n")
    
    # | Entrada | Saída           | Explicação
    # |---------|----------------|-------------------------------
    # | 9       | multiplo de 3  | >0 ✅ e múltiplo de 3 → "multiplo de 3"
    # | 4       | par nao multiplo| >0 ✅ e não múltiplo → "par nao multiplo"
    # | 0       | negativo ou zero| >0 ❌ → "negativo ou zero"
    # | -6      | negativo ou zero| >0 ❌ → "negativo ou zero"

# ===================
# Painel de questões
# ===================

while True:
    print("Escolha a questão para testar (1-10) ou 0 para sair:")
    escolha = int(input("Digite sua opção: "))
    
    if escolha == 0:
        print("Teste finalizado")
        break
    elif escolha == 1:
        questao1()
    elif escolha == 2:
        questao2()
    elif escolha == 3:
        questao3()
    elif escolha == 4:
        questao4()
    elif escolha == 5:
        questao5()
    elif escolha == 6:
        questao6()
    elif escolha == 7:
        questao7()
    elif escolha == 8:
        questao8()
    elif escolha == 9:
        questao9()
    elif escolha == 10:
        questao10()
    else:
        print("Opção invalida, tente novamente.\n")