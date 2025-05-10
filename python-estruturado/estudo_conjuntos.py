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

### união
c0 = c1 | c2
print(c1)
print(c2)
print(f'união com c2 = {c0}')

### intersecção

### Iterando


