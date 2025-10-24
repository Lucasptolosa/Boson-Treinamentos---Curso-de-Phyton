#Orientação a objetos: Paradigma de programação 
# Classes e objetos

class Veiculo: #Letra maiuscula inicial por padrão
    def movimentar(self):
        print(f"sou um veículo e me descoloco!")

    def __init__(self,fabricante,modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo              # __ antes da função deriva em um encapsulamento, requer acesso por um método especial
        self.__num_registro = None

    #Setter
    def set_num_registro(self,registro):
        self.__num_registro = registro

    # Getter
    def get_fabr_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}. \n')

    def get_num_registro(self):
        return self.__num_registro
    
class Carro(Veiculo):
    #Método __init__ será herdado
    def movimentar(self):
        print(f"Sou um carro e ando pelas ruas")

class Motocicleta(Veiculo):
    def movimentar(self):
        print(f"Corro muito!")

class Avião(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__cat = categoria
        super().__init__(fabricante, modelo) #A classe da qual o avião herda

    def get_categoria(self):
        return self.__cat
    
    def movimentar(self):
        print(f'Eu voo alto!')
    
if __name__ == '__main__':
    #meu_veiculo = Veiculo('GM', 'Cadllac Escalade')
    #meu_veiculo.movimentar()
    #meu_veiculo.get_fabr_modelo()
    #meu_veiculo.set_num_registro('490312-1')
    #print(f"Registro: {meu_veiculo.get_num_registro()}\n")
    
    #meu_carro = Carro('Volkswagen', 'Polo')
    #meu_carro.movimentar()
    #meu_carro.get_fabr_modelo()

    #seu_carro = Carro('Audi', 'A5 Sportback')
    #seu_carro.movimentar()
    #seu_carro.get_fabr_modelo()

    #moto = Motocicleta('Harley-Davidson', 'Nightster Special')
    #moto.movimentar()
    #moto.get_fabr_modelo()

    meu_aviao = Avião('Boeing', '747', 'Comercial')
    meu_aviao.movimentar()
    meu_aviao.get_fabr_modelo()
    print(f'categoria: {meu_aviao.get_categoria()}')