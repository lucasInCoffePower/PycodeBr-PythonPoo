'''
    Estudo de estrutura de repetições
    
'''

# Laço for: Utilizado para iterar sobre uma estrutura iterável

## Contando até 10
for i in range(0,11):
    print(i)
    
## Enviando email para clientes
clientes = ['Daniele', 'Carlos', 'Daniel', 'Santos']
def enviar_email(cliente):
    '''Procedimento que avisa quando um email é enviado'''
    return 'Email enviado para {}'.format(cliente)
    
for cliente in clientes:
    print(enviar_email(cliente))
    
## enumerate(): Método que retorna o índice dos elementos em uma lista durante a execução do for
for i, cliente in enumerate(clientes):
    print('Envio {}: {}'.format(i, enviar_email(cliente)))

# While(): Estrutura de repetição utilizada quando não se sabe a quantidade de iterações que serão executadas 

## while para quando x for igual a 10
x = 0 # contador
while x!=10:
    x = x+1
else:
    print('x = {}'.format(x))

# break: é uma palavra chave utilizada para interromper um loop;