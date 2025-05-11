'''
    Variáveis de ambiente em python
    
    Definição windows
        - PowerShell : $env:nome_variavel=valor
        - CMD : set nome_variavel=valor
'''

import os # importando funções de biblioteca que controla a API do SO

api_key = os.getenv("API_KEY") # Lendo variável
api_key2 = os.environ.get("API_KEY") # Lendo variável
print(api_key)
print(api_key2)
print(type(api_key)) # Tipo é sempre string
print(len(os.environ)) # Verificando
os.environ["API_KEY"] = "25" # Alterando variável de ambiente
api_key = os.environ.get("API_KEY") # Pegando novo valor
print(api_key) # Lendo novo valor
