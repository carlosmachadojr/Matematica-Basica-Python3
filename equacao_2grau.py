### AUTOR: Carlos H. Machado Jr.

"""
DESCRIÇÃO:

Código em Python 3 para cálculo das raízes (incluindo raizes complexas) de 
funções polinomiais de grau 2 (Equações do Segundo Grau) utilizando a 
Fórmula de Bhaskara. 

"""
# -----------------------------------------------------------------------------

##### INÍCIO DO PROGRAMA ######################################################

from math import sqrt

p = 2      # número de casas decimais

# -----------------------------------------------------------------------------

##### VALORES DE ENTRADA FORNECIDOS PELO USUÁRIO ##############################

##### Validação dos valores de entrada

def validacao_numerica(num):
    
    """
    1 - Prepara um valor numérico fornecido pelo usuário via input para 
        aplica-los em operações matemáticas.

    2 - Identifica a inteção do usuário em fornecer um valor do tipo 'integer'
        ou do tipo 'float', fazendo a devida conversão.

    """

    num = str(num)          # variável de entrada e retorno
    num_test = str(num)     # variável de teste
    while True:

        # Entrada de valor nulo, string vazia ('')
        if num == '':
            num = num_test = '0'

            break
        # Verificação da presença simultânea de ponto(s) e de vírgula(s).
        # Em caso positivo, o valor fornecido não é um valor numérico válido.
        if '.' in num and ',' in num:
            break

        # Eliminação dos espaços (' ')
        if ' ' in num_test:
            num_test = num_test.replace(' ','')

        # Eliminação do sinal negativo ('-')
        if num_test[0] == '-':
            num_test = num_test.replace('-','')

        # Eliminação do ponto, como separador decimal
        # Não se aplica quando há mais de um ponto        
        if num_test.count('.') == 1:
            num_test = num_test.replace('.','')

        # Eliminação da vírgula, como separador decimal
        # Não se aplica quando há mais de uma vírgula          
        if num_test.count(',') == 1:
            num_test = num_test.replace(',','')
            # Substituição da 'vírgula' por 'ponto' na variável de retorno
            # 'num', viabilizando as operações matemáticas
            num = num.replace(',' , '.')
        break

    # Validação do valor fornecido pelo usuário      
    if num_test.isnumeric() == True:
        num = num.replace(' ' , '')
        # Valor válido: identificação do tipo (integer ou float)
        if '.' in num:
            num = float(num)
        else:
            num = int(num)   
    # Valor inválido    
    else:
        print("\nValor '{}' inválido!\n".format(num))
        num = None
    return num

# -------------------------------------

##### Apresentação dos termos da equação

### (MELHORAR!)
def termos_equacao(coef_str, grau, grau_max):

    """
    Função string para apresentação da Equação na tela do terminal com os
    valores fornecidos pelo usuário, considerando simplificações:

    Exemplo: 1.0 x² + (-4.0) x + 2.0 = 0
    Versão simplificada: x² - 4x + 2 = 0
    """

    if str(int(float(coef_str))) == coef_str:
        coef = int(coef_str)
    else:
        coef = float(coef_str)

    coef_str = str(coef)    
    coef_str_abs = str(abs(coef))

    if grau == 2:
        xn = 'x²'
    if grau == 1:
        xn = 'x'
    if grau == 0:
        xn = ''
    
    if grau == grau_max:
        if coef > 0:
            sinal = ''
        if coef < 0:
            sinal = '-'    
    else:
        if coef > 0:
            sinal = ' + '
        if coef < 0:
            sinal = ' - '    

    if coef  == 0:
        termo = ''

    elif abs(coef) == 1:
        if grau == 0:
            termo = sinal + coef_str_abs   
        else:
            termo = sinal + xn   

    else:
        termo = sinal + coef_str_abs + xn  

    return termo

# -------------------------------------

##### Equação do Segundo Grau - Fórmula de Bhaskara

def bhaskara(A , B , C):
    """
    Calcula as raízes de uma Função Polinomial de Grau 2 utilizando a 
    Fórmula de Bhaskara.
    
    Calcula também as coordenadas do Vértice da Parábola.
    """
    
    delta = B ** 2 - 4 * A * C
    termo_1 = - B / (2 * A)
    termo_2 = sqrt(abs(delta)) / (2 * A)

    if delta < 0:   # Delta negativo --> x ∈ C (conjunto dos Números Complexos)
        x1 = str(round(termo_1, p)) +' + '+ str(abs(round(termo_2 , p))) + ' i'
        x2 = str(round(termo_1, p)) +' - '+ str(abs(round(termo_2 , p))) + ' i' 

    else:           # Delta ≥ 0      --> x ∈ R (conjunto dos Números Reais)
        x1 = round(termo_1 + termo_2 , p)
        x2 = round(termo_1 - termo_2 , p)
        xv = round(-B / 2*A , p)     
        yv = round(-delta /(4*A) , p) 

#   Coordenadas do vértice da parábola
    xv = round(-B / (2*A) , p)     
    yv = round(-delta / (4*A) , p) 

    delta = round(delta , p)

    if A > 0:
        concavidade = 'positiva'
    else:
        concavidade = 'negativa'
    
    return (delta, x1 , x2 , xv , yv, concavidade)

# -----------------------------------------------------------------------------

##### VALORES DE ENTRADA FORNECIDOS PELO USUÁRIO ##############################

separador_1 = '\n' + '-'*80 + '\n'
separador_2 = '\n' + '-'*35 + '\n'

print(separador_1)

print(
    "Forneça os valores dos coeficientes 'A', 'B' e 'C' " +
    "para a equação abaixo:\n")

print('f(x) = Ax² + Bx + C = 0\n')

print(
    'Obs.: Para Equações do Primeiro Grau, A = 0. ' +
    'Para Equações do Segundo Grau, A ≠ 0.\n')

while True:

    A_str = input("Coeficiente 'A' = ")
    B_str = input("Coeficiente 'B' = ")
    C_str = input("Coeficiente 'C' = ")

    A = validacao_numerica(A_str)
    B = validacao_numerica(B_str)
    C = validacao_numerica(C_str)

    if A == B == 0:
        print()
        print("Os valores de 'A' e 'B' não podem ser simultaneamente 'zero'\n")
    else:
        break

if A == 0:
    grau_max = 1
    tipo = 'Primeiro Grau'
else:
    grau_max = 2
    tipo = 'Segundo Grau'

# -----------------------------------------------------------------------------

##### MONTAGEM E APRESENTAÇÃO DA EQUAÇÃO ######################################

equacao = ("f(x) = {}x² + {}x + {} = 0".format(str(A) , str(B) , str(C)))

print("\nEquação definida pelos coeficientes fornecidos:")
print(equacao)

print(separador_2)

termo_A = termos_equacao (A , 2 ,grau_max)
termo_B = termos_equacao (B , 1 ,grau_max)
termo_C = termos_equacao (C, 0 ,grau_max)

equacao_r = ("f(x) = {}{}{} = 0\n".format(termo_A , termo_B , termo_C))

print('Equação do {}:'.format(tipo))
print(equacao_r)

# -----------------------------------------------------------------------------

##### CÁLCULO DAS RAÍZES DA EQUAÇÃO ###########################################

if grau_max == 1:   # Condição para ser uma Equação do Primeiro Grau

    x = - C / B
    x = round(x,p)
    print('x = {}'.format(x))

else:               # Condição para ser uma Equação do Segundo Grau

    calculo = bhaskara (A, B, C)

    delta = calculo[0]
    x1    = calculo[1]
    x2    = calculo[2]
    xv    = calculo[3]
    yv    = calculo[4]

    print("Valor de Delta:")
    print('Δ  = {}\n'.format(delta))

    if delta == 0:
        print("Raíz da função: (x ∈ R)")
        print('x = {:5}'.format(x1))

    else:
        if delta > 0:
            print("Raízes da função: (x ∈ R)")
        else:
            print("Raízes da função: (Números Complexos, x ∈ C)")
        print('x1 = {:5}'.format(x1))
        print('x2 = {:5}'.format(x2))

    print("\nVértice da funçao:")
    print('xv = {:5}'.format(xv))
    print('yv = {:5}'.format(yv))

print(separador_1)   

##### FIM DO PROGRAMA #########################################################
