'''
    Estudo de herança
        ## Definição
            Pilar do POO que é utilizado para criar códigos onde classes podem herdar atributos e funções de outras classes
        ## Vantagens
        - Forma de aproveitar um código já reescrito;
        - Manutenção de código é simplificada;    
        - 
    Classe:
        Abstração de um carro
        
    Propriedades da classe: O que ele é
        - Representado por atributos
    Ações: O que ele faz
        - Representado por métodos ou funções
'''


class Carro:
    # atributos de classe 
    numero_rodas = 4
    quantidade_passageiros = 5
    
    
    # Métodos de classe
    def acelera(self):
        print('Acelerando...')
    
        
    def buzinar(self):
        print('Buzinando...')
        
    
    def frear(self):
        print('Freando...')
    


class Uno(Carro): # Uno herda carro: herda métodos e atributos;
    
    # Atributos próprios do Uno; Herda os demais;
    modelo = 'Uno'
    marca = 'Fiat'
    ano = 1992
    quantidade_passageiros = 4
    
    # Método
    
    def acelera(self):
        print('Uno acelerando...')


if __name__ == '__main__':
    carro = Carro()
    carro.acelera()
    uno = Uno()
    uno.acelera()
    print(uno.quantidade_passageiros) # Acessando atributos
    print(uno.marca)
