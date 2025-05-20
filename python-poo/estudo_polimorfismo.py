'''
    Estudo polimorfismo de classe ou por herança
    
    ## Definição de polimorfismo
        Ideia de que classes diferentes que herdam de outra classe, possam ter métodos que executam ações diferentes mantendo o mesmo identificiador.
        Faz uma associação com herança, de forma que funções identicas em classes mãe e e filha façam ações diferentes;
    
'''


class Animal:
    # Classe que abstrai comportamentos de animais
    
    # Comportamentos
    
    def emitir_som(self):
        print('emite som....')
        
        
class Cachorro(Animal):
    

    # método
    def emitir_som(self):
        print('Au Au ...')


class Gato(Animal):
    
    def emitir_som(self):
        print('Miau ...')


if __name__ == '__main__':
    dog = Cachorro()
    cat = Gato()
    dog.emitir_som()
    cat.emitir_som()
    