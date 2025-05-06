'''
    Estudo de lista
'''

# criando lista
lista1 = [] # lista vazia
lista2 = list() # lista vazia
lista3 = [1,2,3] # lista com números
print(lista1)
print(lista2)
print(lista3)

# .append(): Adicionar elementos no final da lista
carros = []
carros.append('fusca')
carros.append('Jipe')
print(carros)

# .insert(): Inserir um dado em determinada posição da lista baseado no índice
nomes = ['Carla', 'Mateus', 'João']
print(nomes)
nomes.insert(1, 'Daniela')
print(nomes)

# .pop(): Remove o último elemento da lista
nomes = ['Carla', 'Mateus', 'João']
print(nomes)
nomes.pop()
print(nomes)

# del lista: remove um elemento de acordo com o índice
nomes = ['Carla', 'Mateus', 'João']
print(nomes)
del nomes[0]
print(nomes)

# .remove(): Remove um elemento de acordo com o valor. (se tiver mais de um mesmo valor, remove o primeiro)
nomes = ['Carla', 'Daniele', 'Carla']
print(nomes)
nomes.remove('Carla')
print(nomes)

# .count(): Conta a quantidade de elementos dentro de uma lista
nomes = ['Carla', 'Daniele', 'Carla']
print(nomes.count('Carla'))

# .rever(): Inverte a ordem dos elementos em uma lista
nomes = [1,2,3,4,5]
print(nomes)
nomes.reverse() # retorna None
print(nomes)

# Ordenar a lista de forma alfanuméria
nomes = ['Carla', 'Daniele', 'Carla']
numeros = [1,0,5,3,10,2]
misto = [1, 'Carla', 2.5, 3, 'Dan']
print(nomes)
print(numeros)
print(misto)
nomes.sort()
numeros.sort()
misto.sort()
print(nomes) # ordena por ordem alfabética
print(numeros) # ordena por ordem numérica crescente.
# print(misto) -> Dá erro porque internamente a forma como o python ordena a lista é fazendo comparações entre os elementos, e como não é possível compara str com int, resulta emum erro

