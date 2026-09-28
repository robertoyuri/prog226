class Animal:
    def __init__(self, nome, especie, som):
        self.som = som
        self.nome = nome
        self.especie = especie

    def emitir_som(self):
        print(self.som)

cachorro = Animal("rex", "cachorro","au au")
gato = Animal("garfield", "gato", "atchim")
cachorro.emitir_som()
gato.emitir_som()