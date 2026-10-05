class Camada:
    def __init__(self, nome, sistema_cordenadas):
        self.nome = nome
        self.sistema_cordenadas = sistema_cordenadas

    def exibir(self):
        print(self.nome +" "+ self.sistema_cordenadas)

class Cordernadas(Camada):
    def __init__(self, nome, sistema_cordenadas, x, y):
        super().__init__(nome, sistema_cordenadas)
        self.x = x
        self.y = y

    def exibir(self):
        print(self.nome +" "+ self.sistema_cordenadas +" "+ self.x +" "+ self.y)

c = Cordernadas("will","gato","8,5" ,"7,4")
c.exibir()