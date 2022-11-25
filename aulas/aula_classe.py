#hard coded -  é algo que foi escrito diretamente no código.
#self.nome = 'Fusca'#hard coded, escrevi na mão 
#Métodos em instância de classes python. 
#Classe - Mold (geralmente sem dados)
#Instância da class (objeto) -- Tem os dados. 
#Uma classe pode gerar várias instâncias
#Na classe o self é a própria instância. 
class Carro():
    '''Falando da instancia da classe__init_, sempre que 
    começar uma nova instância dentro de uma classe começa com init.'''
    def __init__ (self, nome ) -> None:
        ''' Self é o próprio fusca, toda vez que criar dentro da classe o self é o fusca.  '''
        self.nome = nome #hard coded, escrevi na mão 

        
    def acelerar(self):
        print(f'{self.nome} está acelerando ...')


fusca = Carro('Fusca')#Esse fusca é o self, e o nom
fusca.acelerar()


celta = Carro(nome='Celta')
print(celta.nome)