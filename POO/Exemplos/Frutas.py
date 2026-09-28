class Fruta:
    def __init__(self, nome,cor):
        self.nome = nome
        self.cor = cor
    def amadurecimento(self):
        self.cor = 'marrom'

    def mostrar(self):
        print(f'{self.nome} {self.cor}')

manga = Fruta("Manga", "Amarela")
manga.mostrar()
manga.amadurecimento()
manga.mostrar()

