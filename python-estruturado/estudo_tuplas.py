'''
    Estudo tuplas
'''

# tuplas: Coleções ordenadas, imutáveis, heterogênea, que permitem valores duplicados, e que é iteráveis

## criando tupla
frutas = ('banana', 'maçã', 'pera')
print(frutas) 
nomes = tuple(('Daniele', 'Carlos', 'Pam'))
print(nomes, type(nomes))

## criando tupla com apenas 1 item (obrigatório colocar uma vírgula)
carros = ('van',)
print(carros)

## Verificando quantidade de elementos
print(len(frutas))

## type(tupla): verificar tipo do elemento
print(type(carros))

## .count(value): contar quantidade de determinado elemento
pessoas = tuple(('Daniel', 'Carlos', 'Maria', 'Daniel', 'Santos'))
print(f'tupla: {pessoas}; Tipos {type(pessoas)}' )
print('Quantidade de "Daniel: {}'.format(pessoas.count('Daniel')))

## .index(valor, inicio, fim): retornar o índice de um ocorrência. 
pessoas = tuple(('Daniel', 'Carlos', 'Maria', 'Daniel', 'Santos', 'Daniel'))
print(f'tupla: {pessoas}; Tipos {type(pessoas)}' )
print('Ocorrência de "Daniel: {}'.format(pessoas.index('Daniel',4)))

## "elemento" in tuple: Verificando se há um elemento dentro da tupla. Retorna True ou False
print( 'Carlo' in pessoas)

# Operações com tupla
carros = ('Fiat', 'Chevrolet', 'Fiat Uno')
motos = ('Honda', 'Pop 100')

## Desempacotamento
c1, c2, c3 = carros
print(c1, c2, c3)

## Concatenação
veiculos = carros + motos
print(veiculos)

## Repetição
motos2 = motos * 3
print(motos2)

## Slice 
print(pessoas)
print(pessoas[1:4:2])