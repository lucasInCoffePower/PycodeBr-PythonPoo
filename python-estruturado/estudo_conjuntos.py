'''
    Conjuntos 
'''

# Conjuntos: Uma coleção não ordenável, mutável e que não permite elementos duplicados; Ele é iterável.
#  

## Criação do zero
set1 = {1,2,3,4,5} 
# set2 = set(1,2,3,4) -> Dá erro; Só funciona para converter um iterável
set2 = set([1,2,3,4])
set3 = set('carros') # converte a string em um conjunto com os caracters; Ordem aleatória
print(set1)
print(set2)
print(set3)

## Métodos

### .add(elem): Adiciona elementos;
pessoas = {'daniele', 'carla'}
print(pessoas)
pessoas.add('João')
print(pessoas)
pessoas.add('João') # Tentando adicionar joão novamente; Não adiciona
print(pessoas) # Não permite elementos duplicados

### .update(iteravel): Adiciona ao conjunto outros elementos de um iterável 
dispositivos = set(['telefone', 'mouse', 'smartphone'])
print(dispositivos)
dispositivos.update(['fones de ouvido', 'microfone'])
print(dispositivos)

### .remove(elemento): Remove um elemento do conjunto. Se o elemento não existir, causa erro
dispositivos = set(['telefone', 'mouse', 'smartphone'])
print(dispositivos)
dispositivos.remove('telefone')
print(dispositivos)
# dispositivos.remove('carregador') - Retorna um KeyError

### .discard(elemento): Remove um elemento do conjunto. Não causa erro se o elemento não existir.
dispositivos = set(['telefone', 'mouse', 'smartphone'])
print(dispositivos)
dispositivos.discard('mouse')
dispositivos.discard('teclado')
print(dispositivos)

### .pop(): Remove um elemento aleatório e o retorna
dispositivos = set(['telefone', 'mouse', 'smartphone'])
print(dispositivos)
elemento_removido = dispositivos.pop()
print(dispositivos)
print(elemento_removido)

### .clear(): remove todos os elementos do conjunto
dispositivos = set({'telefone', 'mouse', 'smartphone'})
print(dispositivos)
dispositivos.clear()
print(dispositivos)

### .copy(): Copia os elementos de um conjunto para outra variável, criando um novo conjunto.
dispositivos = set(['telefone', 'mouse', 'smartphone'])
dispositivos2 = dispositivos.copy()
dispositivos2.clear() # removendo todos os elementos de dispositivos2
print(dispositivos2)
print(dispositivos) # não afeta o outro conjunto

### len(conjunto): Retorna a quantidade de elementos que há no conjunto
dispositivos = set(['telefone', 'mouse', 'smartphone'])
print(dispositivos)
print(len(dispositivos))

## Operações: Cada operação gera um novo conjunto
print('################Operações com conjuntos#################')
### conjuntos utilizados
c0 = set() # conjunto vazio
c1 = {1,3,6}
c2 = {2,5,7}
c3 = {1,5,0}

### união ' conjunto1 | conjunto2'
c0 = c1 | c2 # c1.union(c2)
print(c1)
print(c2)
print(f'c1 união com c2 = {c0}')

### intersecção
c0 = c1 & c3 # c1.intersection(c3)
print(c1)
print(c3)
print('c1 intersecção com c3 = {}'.format(c0))

### Diferença: Elementos que estão em um conjunto mas não estão no outro
c0 = c2 - c3 # c2.difference(c3)
print(c2)
print(c3)
print('diferença entre c2 e c3 (elementos que estão em c2 mas não estão em c3) = {}'.format(c0))
print('diferença entre c3 e c2 (elementos que estão em c3 mas não estão em c2) = {}'.format(c3-c2))

### Diferença simétrica: elementos dos conjuntos que só pertencem a um deles.
c0 = c1^c3 # c1.symmetric_difference(c3)
print(c1)
print(c3)
print(f'A diferença simétrica entre c1 e c3 = {c0}') 

### Subconjunto: Identificando se um conjunto e subconjunto de outro. Retorna um tipo booleano
c0 = c1 | c2
print(f'c1({c1}) união c2({c2}) = c0({c0}) logo, c1 é subconjunto de c0 : {c1 <= c0}') # c1.issubset(c0)

### Superconjunto: Identificando se um conjunto é superconjunto de outro. Retorna um tipo booleano
c0 = c1 | c2 
print(f'c1({c1}) união c2({c2}) = c0({c0}) logo, c0 é superconjunto de c1 : {c0 >= c1}') # c0.issuperset(c1)

### Disjunto: Se não há nenhum elemento em comum entre os . Retorna um booleano
print(f'c1 - {c1} - e  c2 - {c2} - são disjuntos entre si? : {c1.isdisjoint(c2)}')
print(f'c1 - {c1} - e  c3 - {c3} - são disjuntos entre si? : {c1.isdisjoint(c3)}')

### Iterando: Retorna aleatoriamente
carros = {'Fiat', 'Palho', 'Chevrolet'}
print(carros)
for carro in carros:
    print(carro)
    
### Pertencimento: elemento in conjunto; elemento in not conjunto; É um teste muito rápido em conjuntos
print(f'Fiat está em {carros} ? {'Fiat' in carros}')
print(f'Fiat não está em {carros} ? {'Fiat' not in carros}')


print('#################Frozenset####################')
# Fronzenset: é um tipo de conjunto que é imutável após a sua criação;
# Não possui nenhum método que o altera; Entretanto, é passível de todas as operações de conjuntos

## frozenset(iteravel): cria um conjunto a partir de outro
fs0 = frozenset() # cria vazio
fs1 = frozenset([1,2,3]) # cria a partir de uma lista
fs2 = frozenset({1,2,3}) # Cria a partir de outro conjuneto
fs3 = frozenset({'a':2, 'b':3}) # Cria a partir de um dicionario; Utiliza apenas as 'keys'
print(fs0) 
print(fs1) 
print(fs2)
print(fs3) 
print(type(fs0)) # da classe frozenset e não mais set

