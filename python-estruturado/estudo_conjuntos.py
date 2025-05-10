'''
    Conjuntos 
'''

# Conjuntos: Uma coleção não ordenável, mutável e que não permite elementos duplicados;
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

### 

## Operações

### Iterando


