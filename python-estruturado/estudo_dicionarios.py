'''
    módulo de estudo de dicionários e seus métodos

    # Definição
        São estruturas de dados definida por chave-valor (key-word), mutável, não ordenada, que não permite chaves duplicadas.
        As chaves podem ser de qualquer tipo primitivo não repetidos, e os valores podem ser de qualquer tipo; 
'''

# Criando dicionários

meu_dici0 = {} # criando dicionario vazio
meu_dici1 = dict() # criando dicionario vazio
meu_dici2 = {'nome': 'Felipe', 'idade': 25, 'profissao': 'engenheiro'} # criando dicionario com elemntos
meu_dici3 = dict(nome='Felipe', idade = 25, profissao='engenheiro') # criando direto de construtor
print(meu_dici0)
print(meu_dici1)
print(meu_dici2)
print(meu_dici3)

# Acessando elementos no dicionário
pessoa = dict(nome='Felipe', idade = 25, profissao='engenheiro') # criando direto de construtor

## Usando chaves: dicionario[chave]
print(f'######Dados##### \n Nome: {pessoa['nome']}\n Idade: {pessoa['idade']} anos \n Profissão: {pessoa['profissao']}') 

## dicionario.get(key): Acessando valor por método get
print('######Dados##### \n Nome: {} \n Idade: {} \n Profissão: {}'.format(pessoa.get('nome'), pessoa.get('idade'), pessoa.get('profissao'))) 

## Iterando sobre dicionário

### Iterando e obtendo chaves
for chave in pessoa:
    print(chave)
    
### Iterando e obtendo chaves: dicionario.keys() -> Retorna um tipo dict_keys - um iterável - com as chaves
for chave in pessoa.keys():
    print(chave)
    
print(pessoa.keys(), type(pessoa.keys()))
print(type(pessoa.keys()))

### Iterando e obtendo valores: dicionario.values() -> Retorna um tipo dict_values - um iterável - com os valores
for valor in pessoa.values():
    print(valor)

print(pessoa.values(), type(pessoa.values()))

# Adicionando elementos ao dicionário
pessoas = dict(nome='Felipe', idade= 25, profissao= 'engenheiro')
print(pessoas)
pessoas['genero'] = 'masculino'
print(pessoas)

# Métodos dicionários
pessoas = dict(nome='Felipe', idade= 25, profissao= 'engenheiro')


## dicionario.pop(chave): Remove um elemento do dicionário e o retorna
print(pessoas.pop('nome'))
print(pessoas)

## dicionario.popitem(): Remove o último item inserido no dicionário; Versão 3.7 do python
pessoas = dict(nome='Felipe', idade= 25, profissao= 'engenheiro')
pessoas.popitem()
print(pessoas)

## dicionario.keys(): Retorna um tipo dict_keys - iterável - com as chaves do dicionário
pessoas = dict(nome='Felipe', idade= 25, profissao= 'engenheiro')
print(pessoas.keys())

## dicionario.values(): Retorna um tipo dict_values - iterável - com os valores do dicionário
print(pessoas.values())

## dicionario.items(): Retorna um tipo_dict_items - iterável - com as chaves e os valores em uma tupla 
print(pessoas.items())


## dicionario.clear() : Remove todos os valores e chaves dos dicionários; Retorna um None
pessoas = dict(nome='Felipe', idade= 25, profissao= 'engenheiro')
pessoas.clear()
print(pessoas)

## dicionario.copy() : gerar um cópia do dicionário com outro endereço de memória
pessoas = dict(nome='Felipe', idade= 25, profissao= 'engenheiro')
pessoas2 = pessoas.copy()
print(pessoas2) 

## dicionario.update(dicionario) : Adiciona ao dicionário os pares de outro dicionário

## dicionario.setdefault(): Retorna um valor associado a uma chave. Se a chave não existir, cria um par chave-valor com ela e com o valor de None;
pessoas = dict(nome='Felipe', idade= 25, profissao= 'engenheiro')
pessoas.setdefault('nome')
print(pessoas)
pessoas.setdefault(25)
print(pessoas)
