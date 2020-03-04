
def validacao_numerica(num):
    
    """
    1 - Prepara um valor numérico fornecido pelo usuário via input para 
        aplica-los em operações matemáticas, realizando as seguintes ações:

        a - exclusão de eventuais espaços antes, após e entre os dígitos;
        b - substituição de 'vírgula' (,) por 'ponto' (.);
        c - atribuição do valor 0 (zero) para entradas de valor nulo.

    2 - Identifica o tipo numérico ('float' ou 'integer') do valor fornecido
        pelo usuário, fazendo a devida conversão.

    3 - Identifica como 'valor inválido' retornando com o valor 'None' quando 
        houver a presença de:

        a - algum caracter não numérico, exceto o sinal de negativo (-), 
            utilizado uma única vez, no início do número; 
        b - 'vírgula' e 'ponto' usados simultaneamente;
        c - mais de uma 'vírgula' ou mais de um 'ponto'.
    
    Obs.:
        i   Nos casos '3a' e '3b' subentende-se um erro de digitação, e não uma
            tentativa de usar o ponto ou a virgula como separador decimal
            Outra possibilidade é que o usuário tenha tentado usar um caracter
            como separador decimal e o outro como separador de milhares;
        ii  Não utilize, portanto, separador(es) de milhares;
        iii A própria linguagem Python possui um atributo para verificação
            numérica (.isnumeric()), entretanto ele só retorna como Verdadeiro os
            números inteiros positivos e o zero. Números decimais e negativos
            ele retorna como Falso. Esta função cria uma variável de teste para
            preparar o valor fornecido, eliminando o sinal negativo e o
            separador decimal, para a verificação pelo '.isnumeric().

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


###############################################################################

print('\nEXEMPLOS:')

valor_1 = '1,5'
valor_1a = validacao_numerica(valor_1) 

valor_2 = '1 500'
valor_2a = validacao_numerica(valor_2) 

valor_3 = ''
valor_3a = validacao_numerica(valor_3) 

valor_4 = '2.3'
valor_4a = validacao_numerica(valor_2) 

valor_5 = '3'
valor_5a = validacao_numerica(valor_3) 

print("\n- O usuário fornece o valor {} e o computador registra {}, "
    .format(valor_1 , valor_1a) + "usando o 'ponto' como separador decimal.")

print("\n- O usuário fornece o valor {} e o computador registra {}, suprimindo"
    .format(valor_2 , valor_2a) + " o(s) espaço(s) entre os dígitos.")

print("\n- O usuário pressiona ENTER e o computador registra o valor {} (zero)"
    .format(valor_3a) +" ao invés de uma string vazia ('{}').".format(valor_3))

print("\n- O usuário fornece o valor {} e o computador registra como um número"
    .format(valor_4) + " do tipo float.")

print("\n- O usuário fornece o valor {} e o computador registra como um número"
    .format(valor_5) + " do tipo 'integer' (int).")

print()



