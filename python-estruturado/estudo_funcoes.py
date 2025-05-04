"""
Estudo de funções e procedimentos

"""

# função nativa (built-in): Qualquer função que já vem instalada por padrão no python
# print é uma função nativa que recebe como argumento uma string ou variável

# Funções personalizadas

def minha_funcao():
    '''Procedimento de apresentação'''
    print('Essa é minha função')


def somar(a, b):
    '''Função que soma dois valores'''
    resultado = a + b
    return resultado


def envia_email():
    '''Procedimento que executa a ação de enviar um email'''
    email = 'pycode@gmail.com'
    senha = '1234'
    # Lógica para enviar o email
    print('Email enviado!')
    
def envia_email_complexo(nome_destinatario: str, email_destinatario: str):
    '''
        Função que envia um email
        Recebe uma string para nome: nome do destinatário
        Recebe uma string para email: email do destinatário
    '''
    nome = nome_destinatario
    email = email_destinatario
    return f'Email enviado para {nome} no email {email_destinatario}'

# Chamando funções criadas

minha_funcao()
print(somar(2, 3))
envia_email()
print(envia_email_complexo('Daniel', 'daniel@email.com'))

nomes = ['Daniele', 'Lucas', 'Tiago']
for nome in nomes:
    print(envia_email_complexo(nome, f'{nome.lower()}@email.com'))






