class Carro:
    def __init__(self, cor, marca, ano, status, velocidade):
        self.cor = cor
        self.marca = marca
        self.ano = ano
        self.status = status
        self.velocidade = velocidade

    def ligar(self):
        self.status = 'LIGADO'

    def desligar(self):
        self.status = 'DESLIGADO'

    def acelerar(self):
        self.velocidade = self.velocidade + 10

    def frear(self):
        self.velocidade = self.velocidade - 10

    def exibir(self):
        print(f'Cor: {self.cor}')
        print(f'Marca: {self.marca}')
        print(f'Ano: {self.ano}')
        print(f'Status: {self.status}')
        print(f'Velocidade: {self.velocidade}')


meu_primeiro_objeto = Carro("Azul", "Honda", "2019", "Desligado", 0)
meu_primeiro_objeto.exibir()
meu_primeiro_objeto.ligar()
meu_primeiro_objeto.exibir()
meu_primeiro_objeto.acelerar()
meu_primeiro_objeto.acelerar()
meu_primeiro_objeto.acelerar()
meu_primeiro_objeto.acelerar()
meu_primeiro_objeto.acelerar()
meu_primeiro_objeto.acelerar()
meu_primeiro_objeto.acelerar()
meu_primeiro_objeto.exibir()

carro_do_benedito = Carro("Preto", "Fiat", "2020", "Desligado", 0)
carro_do_benedito.exibir()
carro_do_benedito.ligar()