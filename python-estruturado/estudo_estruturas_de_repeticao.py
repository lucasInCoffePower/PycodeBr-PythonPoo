'''
    Estudo de estrutura de repetições
    
'''

# Laço for: Utilizado para iterar sobre uma estrutura iterável

# Contando até 10
for i in range(0,11):
    print(i)
    
# Enviando email para clientes
clientes = ['Daniele', 'Carlos', 'Daniel', 'Santos']
def enviar_email(cliente):
    '''Procedimento que avisa quando um email é enviado'''
    return 'Email enviado para {}'.format(cliente)
    
for cliente in clientes:
    print(enviar_email(cliente))
    
# enumerate(): Método que retorna o índice dos elementos em uma lista durante a execução do for
for i, cliente in enumerate(clientes):
    print('Envio {}: {}'.format(i, enviar_email(cliente)))