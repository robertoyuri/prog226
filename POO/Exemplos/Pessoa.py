class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar (self):
        print("Fala mano! Sou " + self.nome)

    def mostrar_idade (self):
        print("Tenho " + str(self.idade) + " anos de idade")

millena = Pessoa ("Millena", 18)
tamires = Pessoa ("Tamires", 19)

millena.cumprimentar()
tamires.cumprimentar()

millena.mostrar_idade()


