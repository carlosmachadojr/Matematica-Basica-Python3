
def virgula_ponto(num):  # Substitui vírgula por ponto, e vice-versa
    """
    Substitui a 'vírgula' (,) por 'ponto' (.) em um número, e vice-versa

    1 - O usuário fornece um valor usando a 'vírgula' como separador decimal.
        A função substitui a 'vírgula' por 'ponto', tornando viáveis, operações
        matemáticas com este valor.
        Entrada: string  // Saída: float

    2 - O usuário fornece um valor usando o 'ponto como separador decimal.
        A função substitui o 'ponto' por 'vírgula', o que é bastante útil para
        apresentação do valor na tela.
        Entrada: float ou string  // Saída: string
    
    Obs.: A função não funciona se o valor fornecido:
        i   - conter 'vírgula' e 'ponto'.
        ii  - conter mais de uma 'vírgula' ou mais de 'ponto'
        iii - conter algum caracter não-numérico
        
        Em todos esses casos o valor retornado é o mesmo valor fornecido.
        Não utilize separadores de milhares.
        Espaços antes, depois ou entre os dígitos são suprimidos. 

    """
    while True:

        # Exceção i: valor contém vírgula e ponto
        if ',' in str(num) and '.' in str(num):
            break

        # Exceção ii: valor contém mais de uma vírgula ou mais de um ponto   
        if str(num).count(',') > 1 or str(num).count('.') > 1:
            break

        # Exceção iii: valor contém caracter não-numérico
        num_ns = str(num).replace(' ','')        
        if str(num_ns).replace('.','').replace(',','').isnumeric() == False:
            break

        # Caso 1: substitui 'vírgula' por 'ponto' (string -> float)
        if ',' in num_ns:
            num_ns = float(num_ns.replace(',' , '.')) 

        # Caso 2: substitui 'ponto' por 'vírgula' (float/string -> string) 
        if '.' in str(num):
            num_ns = str(num_ns).replace('.' , ',')
        num = num_ns

        break
    return num
 
print('\nEXEMPLO:')

valor_1 = '2,5'
valor_1a = virgula_ponto(valor_1) 

valor_2 = '2.5'
valor_2a = virgula_ponto(valor_2) 

print()

print("- O usuário fornece o valor um decimal separado por 'vírgula' e a")
print("  função substitui esta 'vírgula' por um 'ponto', viabilizando a ")
print("  realização de operações matemáticas.")
print('\n\t{} → {}'.format('23,6' , virgula_ponto('23,6')))

print()

print("- O computador apresenta como resultado final, um número decimal ")
print("  separado por 'ponto' e a função substitui este 'ponto' por uma ")
print("  vírgula para apresentação do resultado em tela.")
print('\n\t{} → {}'.format(84.96 , virgula_ponto(84.96)))

print()
