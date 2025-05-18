'''
    Polimorfismo de interface ou ducktyping
    
    Classes diferentes implementam comportamentos com a mesma assinatura, sem precisar de herança.
    Dessa forma, é possível chamar a mesma função variando apenas o objeto utilizado.
    Duck typing: "Se anda como um pato e grasna como um pato, é um pato."


'''



class CalculadoraCientifica:
    # Classe que abstraí o comportamento de uma calculadora científica
    
    def somar(self, n1, n2):
        return n1 + n2 
    
    
class CalculadoraBasica:
    # Classe que abstraí o comportamento de uma calculadora básica
    
    def somar(self, n1, n2):
        return n1 + n2
    
    
class Matematico:
    # classe que abstraí o comportamento de um matemático
    
    # atributos
    
    def __init__(self, calculadora=None):
        
        self.calculadora = calculadora
    
    # métodos de classe
    
    
    def pegar_cientifica(self, tipo_calculadora):
        self.calculadora = tipo_calculadora
    
    def pegar_basica(self, tipo_calculadora):
        self.calculadora = tipo_calculadora
    
    def somar(self, n1, n2):
        return self.calculadora.somar(n1, n2)
    
    def calculadora_usada(self):
        print(f'{type(self.calculadora)}')

if __name__ == '__main__':
    cientifica = CalculadoraCientifica()
    basica = CalculadoraBasica()
    matematico = Matematico()
    matematico.calculadora_usada()
    matematico.pegar_cientifica(cientifica)
    matematico.calculadora_usada()
    print(matematico.somar(2,3)) # visualizando consequência do ducktyping
    matematico.pegar_basica(basica)
    print(matematico.somar(2,3)) # visualizando consequência do ducktyping