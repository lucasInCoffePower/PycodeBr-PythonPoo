# Arquivo para estudo de operadores lógicos e operadores relacionais

# Operadores lógicos: not, and, or
# Operadores relacionais: !=, ==, >, <, >=, <=

# Análise da condição com and
a = True
b = False

if a and b:
    print('Atendeu a condição!')
else:
    print('Não atendeu a condição!')
    
# Análise da condição com or
c = True
d = False

if c or d:
    print('Atendeu a condição!')
else:
    print('Não atendeu a condição!')
    
# Verificando se um valor é igual ao outro: operador de igualdade
idade = 25
nome = 'Felipe'
if idade == 25:
    print('Idade correta!')
else:
    print('idade incorreta!')
    
# Testando operador de negação
if idade != 25:
    print('Idade correta!')
else:
    print('Idade incorreta!')
    
# Testando nome e idade com or e !=
if nome == 'Felipe' or idade != 25:
    print('Dados corretos!')
else:
    print('Dados incorretos!')
    
# Condicional mais complexa
nome = 'Daniel'
idade = 50
peso = 69

# O or tem menor prioridade sobre o and: todos os and são executados, depois o or é executado
if peso == 69 or nome == 'Daniel' and idade == 40: 
    print('Dados corretos!')
else:
    print('Dados incorretos!')
    
    
# O or tem menor prioridade sobre o and: todos os and são executados, depois o or é executado
if peso == 69 or nome == 'Daniel' and idade == 40: 
    print('Dados corretos!')
else:
    print('Dados incorretos!')


    
