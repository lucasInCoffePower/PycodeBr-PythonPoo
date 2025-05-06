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

# 