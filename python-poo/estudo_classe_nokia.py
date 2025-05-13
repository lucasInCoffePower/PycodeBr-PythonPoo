'''
    Classe que representa o comportamento de um celular nokia tijolão
'''


class Celular:
    # atributos
    marca = 'Nokia'
    modelo = 'Tijolão'
    cor = 'azul'
    tem_camera = False
    bateria =  'infinta'
    
    # métodos da classe
    def fazer_ligacoes(self):
        print('Fazendo ligações...')
        
    def fazer_cobrinha(self):
        print('Jogando cobrinha...')
        
    def despertador(self):
        print('Despertando ...') 
        
    def calcular(self, v1, v2):
        return v1+v2
        

# criando uma instancia de classe
celular = Celular()


print(celular) # mostra o endereço da classe
print(celular.modelo) # mostrando propriedade
celular.despertador() # executando função
print(celular.calcular(2,3))