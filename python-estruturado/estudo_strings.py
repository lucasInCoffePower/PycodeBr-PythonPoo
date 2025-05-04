# slicing:  percorrer a string e retorna uma substring
texto = 'AULA PYCODEBR'
print(texto[0]) # Retorna o elemento da posição 1 e de índice 0
print(texto[4]) # Retorna o elemento da posição 4 e de índice 3
print(texto[-1]) # Retorna o elemento da última posição, de índice "tamanho da string - 1"
print(texto[5:11]) # Retorna o elementre entre os índices 4 e 10 de intervalo fechado
print(texto[5:13]) # Pega do 4 até o 12
print(texto[5:]) # Pega até o último caractere

# len: Retornando o tamanho da string
print(len(texto))

# count: Retornando a quantidade de uma determinada substring dentro da string
print(texto.count('A'))
print(texto.count('AULA'))
print(texto.count('n'))
print(texto.count('A', 0, 4)) # Contar a quantidade de um caractere entre as posições

# find: Encontrando e retornando o índice de início de uma ocorrência
print(texto.find('A'))
print(texto.find(' '))
print(texto.find('ULA'))

# .upper(): Gerando uma string maiúscula a partir da original (não converte a original)
print(texto.upper()) # conversão
print(texto) # mostrando versão atual

# .lower(): Gerando uma string minúscula partir da original (não converte a original)
print(texto.lower())
print(texto)

# .capitalize(): Tornando apenas a primeira letra maiúscula
print(texto.capitalize())
print(texto)

# .title(): Tornando a primeira letra de cada substring separada por espaço na string em maiúscula
print(texto.title())
print(texto)

# split: Separando uma string em uma lista de strings
print(texto.split()) # por padrão ele separa a string ao encontrar o caractere " " 
print(texto.split('A')) # Separa em string nas ocorrências de 'A'
print(texto.split('b')) # Se for um caractere ausente na string, gera uma lista contendo a string inteira

# join: Unir listas em uma string
lista_de_palavras = ['carro', 'vaca', 'jose']
print(lista_de_palavras)
print(' '.join(lista_de_palavras)) # Junta a lista em uma única string separando os elementos por " " 
print('@'.join(lista_de_palavras)) # Junta a lista em uma única string separando os elementos por @

# strip: Remove os espaços em branco nos extremos da string retornando uma nova string
palavra = " Olá Mundo "
print(palavra)
print(palavra.strip()) 

# rstrip: Remove os espaços em branco do extremo direito da string retornando uma nova string
print(palavra.rstrip())

#lstrip: remove o espaço em brando do extremo esquerdo da string retornando uma nova string
print(palavra.lstrip())

# replace: Substitui um caractere por outro retornando uma nova string
palavra2 = 'Carl itos'
print(palavra2)
print(palavra2.replace(' ',''))

# Somando strings
nome = 'Daniel'
sobrenome = ' Carlos'
print(nome + sobrenome)
